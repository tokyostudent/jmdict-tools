///<reference path="../Scripts/typings/jquery/jquery.d.ts"/>
/*
Handles the text input box where words are entered by user
Words are entered in any language and the output changes accordingly:
* English: shows senses and their readings
* Kana: shows kanji and senses
* Kanji: shows kana and senses
*/
var WordSuggest;
(function (WordSuggest) {
    "use strict";

    var Box = (function () {
        function Box(suggestBox) {
            var _this = this;
            this.suggestBox = suggestBox;
            this._suggestService = AppConfig.wordSuggestService(true);
            this.prevBoxText = suggestBox.val();

            suggestBox.keyup(function () {
                if (_this.prevBoxText !== suggestBox.val()) {
                    _this.prevBoxText = suggestBox.val();
                    _this.onTextChanged(_this.prevBoxText);
                }
            });
        }
        Box.prototype.onTextChanged = function (key) {
            this._suggestService.lookup(key).then(function (results) {
                console.log(results);
                console.log("hara");
            });
        };
        return Box;
    })();
    WordSuggest.Box = Box;
})(WordSuggest || (WordSuggest = {}));
//# sourceMappingURL=Module.js.map
