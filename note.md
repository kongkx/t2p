- Inkscape Command: `inkscape -T -f in.svg -l out.svg`

docker run -it --rm -v /Users/steven/Documents/Projects/inkscape-command:/usr/src/app -p9888:9888 inkscape:ubuntu 


```
RUN buildDeps='gcc libc6-dev make' \
    && apt-get update \
    && apt-get install -y $buildDeps \
    && wget -O redis.tar.gz "http://download.redis.io/releases/redis-3.2.5.tar.gz" \
    && mkdir -p /usr/src/redis \
    && tar -xzf redis.tar.gz -C /usr/src/redis --strip-components=1 \
    && make -C /usr/src/redis \
    && make -C /usr/src/redis install \
    && rm -rf /var/lib/apt/lists/* \
    && rm redis.tar.gz \
    && rm -r /usr/src/redis \
    && apt-get purge -y --auto-remove $buildDeps
  ```


## Svg Font Family

Inkscape 对字体的支持与其他主流的 图形软件有差异，与浏览器的行为也有区别。

不支持: `Courier-Bold` 这样的写法


```svg
<?xml version="1.0" standalone="no"?><!-- Generator: Gravit.io --><svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" style="isolation:isolate" viewBox="0 0 128 128" width="128" height="128">
<defs><clipPath id="_clipPath_9zKFok6jlavoojri1lWT5Qx6U2urBNyF"><rect width="128" height="128"/></clipPath></defs>
<g clip-path="url(#_clipPath_9zKFok6jlavoojri1lWT5Qx6U2urBNyF)">
  <g transform="matrix(1,0,0,1,27,49.5)">
    <text transform="matrix(1,0,0,1,0,22.617)" style="font-family:'Courier';font-weight:700;font-size:30px;font-style:normal;fill:#000000;stroke:none;">TExT</text>
  </g>
</g>
</svg>
```

## HelveticaNeue-CondensedBold 文本样式

preview: 
![](./output_line_TExT.svg)

### Inkscape

```svg
<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<svg
   xmlns:dc="http://purl.org/dc/elements/1.1/"
   xmlns:cc="http://creativecommons.org/ns#"
   xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
   xmlns:svg="http://www.w3.org/2000/svg"
   xmlns="http://www.w3.org/2000/svg"
   id="svg2"
   version="1.1"
   viewBox="0 0 128 128"
   height="128px"
   width="128px">
  <metadata
     id="metadata19">
    <rdf:RDF>
      <cc:Work
         rdf:about="">
        <dc:format>image/svg+xml</dc:format>
        <dc:type
           rdf:resource="http://purl.org/dc/dcmitype/StillImage" />
        <dc:title>TExT-sketch</dc:title>
      </cc:Work>
    </rdf:RDF>
  </metadata>
  <!-- Generator: Sketch 51.3 (57544) - http://www.bohemiancoding.com/sketch -->
  <title
     id="title4">TExT-sketch</title>
  <desc
     id="desc6">Created with Sketch.</desc>
  <defs
     id="defs8" />
  <g
     fill-rule="evenodd"
     fill="none"
     stroke-width="1"
     stroke="none"
     id="Page-1">
    <g
       id="Artboard">
      <g
         id="TExT-sketch">
        <rect
           height="128"
           width="128"
           y="0"
           x="0"
           fill="#FFFFFF"
           id="Rectangle" />
        <text
           fill="#000000"
           font-weight="bold"
           font-style="condensed"
           font-size="58"
           font-family="HelveticaNeue-CondensedBold, Helvetica Neue"
           id="TExT">
          <tspan
             style="-inkscape-font-specification:'Helvetica Neue Bold Condensed';font-family:'Helvetica Neue';font-weight:bold;font-style:normal;font-stretch:condensed;font-variant:normal"
             id="tspan15"
             y="85"
             x="9.313">TExT</tspan>
        </text>
      </g>
    </g>
  </g>
</svg>
```

| generator | inkscape | sketch | Gravit | AI | chrome | firefox | safari |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Inkscape | √ | x | x | √ | x | √ | √ |

### Sketch 

```svg
<?xml version="1.0" encoding="UTF-8"?>
<svg width="128px" height="128px" viewBox="0 0 128 128" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
    <!-- Generator: Sketch 51.3 (57544) - http://www.bohemiancoding.com/sketch -->
    <title>TExT-sketch</title>
    <desc>Created with Sketch.</desc>
    <defs></defs>
    <g id="Page-1" stroke="none" stroke-width="1" fill="none" fill-rule="evenodd">
        <g id="Artboard">
            <g id="TExT-sketch">
                <rect id="Rectangle" fill="#FFFFFF" x="0" y="0" width="128" height="128"></rect>
                <text id="TExT" font-family="HelveticaNeue-CondensedBold, Helvetica Neue" font-size="58" font-style="condensed" font-weight="bold" fill="#000000">
                    <tspan x="9.313" y="85">TExT</tspan>
                </text>
            </g>
        </g>
    </g>
</svg>
```

| generator | inkscape | sketch | Gravit | AI | chrome | firefox | safari | 
| --- | --- | --- | --- | --- | --- | --- | --- | 
| skecth | x | √ | x | x | √ | x | √ |


### AI 

```svg
<?xml version="1.0" encoding="utf-8"?>
<!-- Generator: Adobe Illustrator 19.0.0, SVG Export Plug-In . SVG Version: 6.00 Build 0)  -->
<svg version="1.1" id="图层_1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px"
	 viewBox="-935 937 128 128" style="enable-background:new -935 937 128 128;" xml:space="preserve">
<style type="text/css">
	.st0{fill:#FFFFFF;}
	.st1{font-family:'HelveticaNeue-CondensedBold';}
	.st2{font-size:58px;}
</style>
<title>TExT-sketch</title>
<desc>Created with Sketch.</desc>
<g id="TExT-sketch">
	<rect id="Rectangle" x="-935" y="937" class="st0" width="128" height="128"/>
	<text transform="matrix(1 0 0 1 -925.687 1022)" class="st1 st2">TExT</text>
</g>
</svg>
```

| generator | inkscape | sketch | Gravit | AI | chrome | firefox | safari |
| --- | --- | --- | --- | --- | --- | --- | --- |
| AI | x | x | x | √ | √ | x | √ |
