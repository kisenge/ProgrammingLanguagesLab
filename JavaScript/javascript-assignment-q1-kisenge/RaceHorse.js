import{Horse} from './Horse.js';
import{Saddle} from './Saddle.js';

export class RaceHorse extends Horse{
  constructor(name,age,costToRent,saddle){
    super(name,age,costToRent,saddle);
  this.wins=0
  }


  hasWon(){
    let newWins= this.wins+1;
    this.wins=newWins;
  }


  getRaceHorseInfo(includeWins){
    if(includeWins==true){
      console.log("\n\n\n\nLesson with: "+this.name+" (age: "+this.age+")");
      console.log("\n\tSaddle: "+this.saddle.getMaterial+" (width: "+this.saddle.getWidth+"cm)");
      console.log("\n\tRaces won: "+this.wins);
    }

    else{
      console.log("\n\n\n\nLesson with: "+this.name+" (age: "+this.age+")");
      console.log("\n\tSaddle: "+this.saddle.getMaterial+" (width: "+this.saddle.getWidth+"cm)");
    }

  }

  get getLessonCost(){

    if((this.wins>3) || (this.age<3 && this.wins>2)){
      let cost= this.saddle.getRentCost;
      cost= cost+this.costToRent;
      cost= cost*1.33;
      cost= cost.toFixed(2)
      console.log("\nCost of a lesson: $"+cost);
    }

    else{
      let cost= this.saddle.getRentCost;
      cost= cost+this.costToRent;
      console.log("\nCost of a lesson: $"+cost);
    }


  }




}
