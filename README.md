# PyConCA Websites Archive

## How to download a website

```bash
wget --no-check-certificate --mirror -p --html-extension --convert-links -e
robots=off -P . $URL
```

### How to download 2012 website

PyConCA 2012 website was developed differently than the other years. It requires the language be added in the `Accept-Language` header.

```bash
wget --header='Accept-Language: $LANG' --no-check-certificate --mirror -p --html-extension --convert-links -e robots=off -P . $URL
```

Also the json files.

```bash
wget --header='Accept-Language: $LANG' http://2012.pycon.ca/talk/{1..85}.json
```

## Run the example nginx.conf

```bash
nginx -c nginx.conf -p `pwd`
```

## TODOs

* [ ] 2012.pycon.ca is only showing the French version of the website.
