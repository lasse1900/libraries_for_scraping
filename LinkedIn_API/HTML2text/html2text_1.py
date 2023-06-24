import html2text

output = html2text.html2text('''
<!doctype html>
<html class="no-js" lang="">
    <head>
        <title>Test - A Sample Website</title>
        <meta charset="utf-8">
        <link rel="stylesheet" href="css/normalize.css">
        <link rel="stylesheet" href="css/main.css">
    </head>
    <body>
        <h1 id='site_title'>Test Website</h1>
        <hr></hr>
        <div class="article">
            <h2><a href="article_1.html">Article 1 Headline</a></h2>
            <p>This is a summary of article 1</p>
        </div>
        <hr></hr>
        <div class="article">
            <h2><a href="article_2.html">Article 2 Headline</a></h2>
            <p>This is a summary of article 2</p>
        </div>
        <hr></hr>
        <div id='footer'>
            <p>Footer Information</p>
        </div>
        <script>
        var para = document.createElement("p");
        var node = document.createTextNode("This is text generated by JavaScript.");
        para.appendChild(node);
        var element = document.getElementById("footer");
        element.appendChild(para);
        </script>
    </body>
</html>

''')

print(output)