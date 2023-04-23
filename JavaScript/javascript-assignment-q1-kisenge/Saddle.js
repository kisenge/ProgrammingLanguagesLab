export class Saddle {
  constructor(material,width,rentCost) {
    this.material= material;
    this.width= width;
    this.rentCost=rentCost;
  }

  set changeMaterial(newMaterial){
    this.material=newMaterial;
  }

  set changeAge(newWidth){
    this.width=newWidth;
  }

  set changeRentCost(newRentCost){
    this.costToRent=newRentCost;
  }

  get getMaterial(){
    return this.material;
  }

  get getWidth(){
    return this.width;
  }

  get getRentCost(){
    return this.rentCost;
  }





}
