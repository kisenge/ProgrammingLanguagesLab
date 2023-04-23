%T = readtable('VehicleLocation.csv')
T= importdata("VehicleLocation.csv")
speedy= T.data(:,1)
speedx= T.textdata


lenA=size(speedx)
rowNum=lenA(1,1)


xArr=zeros(rowNum,1)



      



for i= 1:rowNum
   
    xArr(i)=str2double(speedx{i})

end


for i=1:rowNum-1

    distancex(i,1)=abs(xArr(i+1)-xArr(i))
    distancey(i,1)=abs(speedy(i+1)-speedy(i))

    d1= distancex(:,1)
    d2= distancey(:,1)

    D= sqrt(sum((d1 - d2).^2, 2))

end

speed=distance(:,2)
speed(1,:)=[]
s1= D/speed
plot(s1)
xlabel('Time') 
ylabel('Speed Km/hr')