import * as readline from 'node:readline';
import { stdin as input, stdout as output } from 'node:process';
import axios from 'axios';
import fs from 'fs';

var detectedLang="";
var textInput="";
var translatedText="";
var translationLang="";
var string="";
var abbrv=[];

var x=0;
var done=0;



function wordsinCommon(textInput,translatedText){
   var count=0;
   var a= textInput.split(' ');
   var b= translatedText.split(' ');

   for(let l of a){
      if(b.indexOf(l) >= 0){
          count++;
      }
   }
   return count;
}




const content = fs.readFileSync('LanguageOptions.txt');
string= content.toString();




const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});





rl.question('What text would you like to translate?\n', (answer2) => {
    rl.question('What language would you like to translate to?\n', (answer1) => {
        textInput=answer2;
        translationLang=answer1;


        //file stuff
        for (let k=0; k<translationLang.length; k++){
          var g=k;
          if(done==1){
            break;
          }
          for (let i=0; i<string.length; i++){
              var j=i;

              if(string[j]===translationLang[g] && !done){


                while(string[j]==translationLang[g] && !done){
                    //in front
                    if(string[j+1]==="\t"  ){
                      var x=j+1;
                      while(string[x]==="\t"){
                        x=x+1;
                      }
                      var abbrvInc=0;

                      //behind
                      while(string[x]!=" " && !(string[x]==='\n') && !(string[x]==='\r')){

                        abbrv[abbrvInc]=string[x];
                        x++;
                        abbrvInc++;

                      }

                      done=1;

                    }
                    else{
                      j++;
                      g++;
                    }
                }

              }
              if(done==1){
                break;
              }
          }
        }

        abbrv= abbrv.join("");
        var abbrvString= abbrv.toString();
        console.log(abbrvString);




        const encodedParams2 = new URLSearchParams();
        encodedParams2.append("q", textInput);
        encodedParams2.append("target", abbrvString);
        encodedParams2.append("source", "en");

        const options2 = {
          method: 'POST',
          url: 'https://google-translate1.p.rapidapi.com/language/translate/v2',
          headers: {
            'content-type': 'application/x-www-form-urlencoded',
            'Accept-Encoding': 'application/gzip',
            'X-RapidAPI-Key': ,
            'X-RapidAPI-Host': 'google-translate1.p.rapidapi.com'
          },
          data: encodedParams2
        };

        axios.request(options2).then(function (response) {
          translatedText= response.data.data.translations[0].translatedText;
          console.log("Translation is : "+translatedText);
        }).catch(function (error) {
          console.error(error);
        });


        const encodedParams = new URLSearchParams();
        encodedParams.append("q", "I");
        const options = {
          method: 'POST',
          url: 'https://google-translate1.p.rapidapi.com/language/translate/v2/detect',
          headers: {
            'content-type': 'application/x-www-form-urlencoded',
            'Accept-Encoding': 'application/gzip',
            'X-RapidAPI-Key': '',
            'X-RapidAPI-Host': 'google-translate1.p.rapidapi.com'
          },
          data: encodedParams
        };

        axios.request(options).then(function (response) {
          detectedLang= response.data.data.detections[0][0].language;
          console.log("Detected language is " +detectedLang);

        }).catch(function (error) {
          console.error(error);
        });








        console.log("Stats:");

        //need to permanrntly store translatedText for section to work
        var common= wordsinCommon(textInput,translatedText);
        console.log("Common words"+common);



        rl.close();
    });
});
