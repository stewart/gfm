import hashlib, re
import markdown as markdown_lib

def gfm(text):
    """Processes Markdown according to GitHub Flavored Markdown spec."""
    extractions = {}

    def extract_pre_block(matchobj):
        match = matchobj.group(0)
        hashed_match = hashlib.md5(match.encode('utf-8')).hexdigest()
        extractions[hashed_match] = match
        result = "{gfm-extraction-%s}" % hashed_match
        return result

    def escape_underscore(matchobj):
        match = matchobj.group(0)

        if match.count('_') > 1:
            return re.sub('_', '\_', match)
        else:
            return match

    def newlines_to_brs(matchobj):
        match = matchobj.group(0)
        if re.search("\n{2}", match):
            return match
        else:
            match = match.strip()
            return match + "  \n"

    def insert_pre_block(matchobj):
        string = "\n\n" + extractions[matchobj.group(1)]
        return string

    text = re.sub("(?s)<pre>.*?<\/pre>", extract_pre_block, text)
    text = re.sub("(^(?! {4}|\t)\w+_\w+_\w[\w_]*)", escape_underscore, text)
    text = re.sub("(?m)^[\w\<][^\n]*\n+", newlines_to_brs, text)
    text = re.sub("\{gfm-extraction-([0-9a-f]{32})\}", insert_pre_block, text)

    return text

def markdown(text):
    """Processes GFM then converts it to HTML."""
    text = gfm(text)
    text = markdown_lib.markdown(text)
    return text
