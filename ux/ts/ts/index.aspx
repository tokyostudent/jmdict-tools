<!DOCTYPE html>

<html lang="en">
<head>
    <meta charset="utf-8" />
    <title>TypeScript HTML App WTF</title>
    <link rel="stylesheet" href="app.css" type="text/css" />
    
    <script src="Scripts/Promise.js"></script>
    <script src="WordSuggest/FakeService.js"></script>
    <script src="WordSuggest/Model.js"></script>
    <script src="WordSuggest/Module.js"></script>
    <script src="WordSuggest/Service.js"></script>
    <script src="Config.js"></script>
    <script src="app.js"></script>
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta name="description" content="The description of my page" />
</head>
<body>
    <h1>TypeScript HTML App</h1>

    <div id="content"></div>
    <input class="suggestBox" id="suggestBox" autofocus/>

    <div class="resultsOutputPane">
        <div class="english" data-bind="style: { visibility: english.length ? 'visible' : 'hidden' }">

        </div>
        <div class="kanji" data-bind="style: { visibility: kanji.length ? 'visible' : 'hidden' }">

        </div>
        <div class="kana" data-bind="style: { visibility: kanji.length ? 'visible' : 'hidden' }">

        </div>
    </div>
    
    <script src="Scripts/jquery-2.1.0.js"></script>
</body>
</html>
