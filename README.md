# PyConCA Websites Archive

## How to download a website

```bash
wget --no-check-certificate --mirror -p --html-extension --convert-links -e
robots=off -P . $URL
```