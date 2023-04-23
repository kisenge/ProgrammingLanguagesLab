import{Saddle} from './Saddle.js';
import{Horse} from './Horse.js';
import{RaceHorse} from './RaceHorse.js';


let saddleCheap= new Saddle("plastic",47,10);
let saddleMid1= new Saddle("Rubber",51,20);
let saddleMid2= new Saddle("Fibreglass",55,25);
let saddleLuxury1= new Saddle("Leather",60,45);
let saddleLuxury2= new Saddle("Synthetic",62,55);


let horse1= new Horse("Black Beauty",6,150,saddleLuxury1);
let horse2= new Horse("Colt 45",2,65,saddleCheap);

//winner and shows
let americanPharaoh= new RaceHorse("American Pharaoh",1,120,saddleLuxury1);



americanPharaoh.hasWon();
americanPharaoh.hasWon();
americanPharaoh.hasWon();
americanPharaoh.hasWon();
americanPharaoh.hasWon();
americanPharaoh.hasWon();
americanPharaoh.hasWon();


//no wins and shows
let seaBiscuit= new RaceHorse("Sea Biscuit",30,110,saddleMid1);

// no wins, no shows
let greatHope= new RaceHorse("Great Hope",5,130,saddleLuxury2)

console.log(horse1.getHorseInfo);
console.log(horse1.getLessonCost);

console.log(horse2.getHorseInfo);
console.log(horse2.getLessonCost);

console.log(americanPharaoh.getRaceHorseInfo(true));
console.log(americanPharaoh.getLessonCost);

console.log(seaBiscuit.getRaceHorseInfo(true));
console.log(seaBiscuit.getLessonCost);

console.log(greatHope.getRaceHorseInfo(false));
console.log(greatHope.getLessonCost);
