///<reference path="../Scripts/typings/jquery/jquery.d.ts"/>

/*
Handles the text input box where words are entered by user
Words are entered in any language and the output changes accordingly:
* English: shows senses and their readings
* Kana: shows kanji and senses
* Kanji: shows kana and senses
*/
module WordSuggest {
    "use strict";

    export class Box {
        private _suggestService:WordSuggest.IService = AppConfig.wordSuggestService(true);
        private prevBoxText:string;
        constructor(private suggestBox: JQuery) {
            this.prevBoxText = suggestBox.val();

            suggestBox.keyup(():void => {
                if (this.prevBoxText !== suggestBox.val()) {
                    this.prevBoxText = suggestBox.val();
                    this.onTextChanged(this.prevBoxText);
                }
        });

        }

        private onTextChanged(key: string):void {
            this._suggestService.lookup(key).then((results:Model):void => {
                console.log(results);
                console.log("hara");
            });


        }
    }
} 