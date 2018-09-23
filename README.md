# SVG Text To Path service

使用 Inkscape 进行转换。

使用方式, CURL as example

```
curl -H 'Authorization: Token DEMO_TOKEN' \
  -F "file=@/path/to/input.svg" \
  http://localhost:9888 > output.svg
```

注意： 

一些特殊字体的属性定义，Inkscape 识别可能存在问题，造成输出结果与预期的不一致。例如`HelveticaNeue-CondensedBold` 的样式。 

如果需要转换这种比较复杂的字体，需要对svg 进行预处理。 

**Inkscape**

- `font-family:'Helvetica Neue'` + `font-weight:bold` + `font-stretch:condensed`: `字体集` + `font-weight` + `font-stretch`

```svg
<tspan
  style="-inkscape-font-specification:'Helvetica Neue Bold Condensed';font-family:'Helvetica Neue';font-weight:bold;font-style:normal;font-stretch:condensed;font-variant:normal"
  id="tspan15"
  y="85"
  x="9.313">TExT</tspan>
```

**Sketch**

`font-style=condensed` 不在svg标准里面, **即使使用sketch也无法识别**

```svg
<text id="TExT" font-family="HelveticaNeue-CondensedBold, Helvetica Neue" font-size="58" font-style="condensed" font-weight="bold" fill="#000000">
    <tspan x="9.313" y="85">TExT</tspan>
</text>
```

**兼容性写法**

```svg
<?xml version="1.0" encoding="utf-8"?>
<svg version="1.0" width="128px" height="128px" viewBox="0 0 128 128" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" xml:space="preserve">
<title>TExT</title>
<g id="TExT">
	<rect id="Rectangle" x="0" y="0" width="128" height="128" fill="#FFFFFF" />
	<text
    x="9.313"
    y="85"
    font-family="HelveticaNeue-CondensedBold, Helvetica Neue"
    font-weight="bold"
    font-stretch="condensed"
    font-size="58px"
  >TExT</text>
</g>
</svg>
```

- `HelveticaNeue-CondensedBold` 可以被`Chrome`, `Illustrator`, `Safari` 识别
- `font-family` + `font-weight` + `font-stretch` 可以被 `Inkscape, Illustrator, Firefox` 识别


## Setup

- prepare fonts, copy fonts to `fonts` folder. 

- build docker image, 
  ```
  docker build -t custom/text-to-path:1 .
  ```

- start service, port depends on config

  ```bash
  docker run  -p 9888::9888 -v my-vol:/usr/src/app  custom/text-to-path
  ```

## References

- [w3c -- Text-FontStyleProperty](https://www.w3.org/TR/SVG11/text.html#FontPropertiesUsedBySVG)