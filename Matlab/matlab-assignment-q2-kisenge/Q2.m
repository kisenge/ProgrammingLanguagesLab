T = readtable('CurveData1.csv');


T(1,2)
a = zeros(1,1)

sz= size(T)
rowNum=sz(1)

xArr= zeros(1,1)
yArr= zeros(1,1)
errSum1= zeros(1,1)
errSum2= zeros(1,1)
errSum3= zeros(1,1)
errSum4= zeros(1,1)
errSum5= zeros(1,1)



for i= 1:rowNum
    x=T{i,1}
    y=T{i,2}
    
    xArr(i,1)=x
    yArr(i,1)=y
end   

%Fit1;
modX = xArr([6:25])
modY = yArr([6:25])
checkX1= xArr([1:5])
checkY1= yArr([1:5])
 

fitobject1 = fit(modX,modY,'poly2')

sz= size(checkX1)
rowNum=sz(1)
for i= 1:rowNum
    est = feval(fitobject1,checkX1(i,1))
    err= abs(est-checkY1(i,1))
    errSum1(i)=err
end
e1= sum(errSum1,2)





%Fit 2; 
modX = xArr([1:5,11:25])
modY = yArr([1:5,11:25])
checkX2= xArr([6:10])
checkY2= yArr([6:10])

fitobject2 = fit(modX,modY,'poly2')

sz= size(checkX2)
rowNum=sz(1)
for i= 1:rowNum
    est = feval(fitobject2,checkX2(i,1))
    err= abs(est-checkY2(i,1))
    errSum2(i)=err
end
e2= sum(errSum2,2)



%Fit 3; 
modX = xArr([1:10,16:25])
modY = yArr([1:10,16:25])
checkX3= xArr([11:15])
checkY3= yArr([11:15])

fitobject3 = fit(modX,modY,'poly2')
sz= size(checkX3)
rowNum=sz(1)
for i= 1:rowNum
    est = feval(fitobject3,checkX3(i,1))
    err= abs(est-checkY3(i,1))
    errSum3(i)=err
end
e3= sum(errSum3,2)



%Fit 4; 
modX = xArr([1:15,21:25])
modY = yArr([1:15,21:25])
checkX4= xArr([16:20])
checkY4= yArr([16:20])

fitobject4 = fit(modX,modY,'poly2')
sz= size(checkX4)
rowNum=sz(1)
for i= 1:rowNum
    est = feval(fitobject4,checkX4(i,1))
    err= abs(est-checkY4(i,1))
    errSum4(i)=err
end
e4= sum(errSum4,2)


%Fit 5; 
modX = xArr([1:20])
modY = yArr([1:20])
checkX5= xArr([21:25])
checkY5= yArr([21:25])

fitobject5 = fit(modX,modY,'poly2')
sz= size(checkX5)
rowNum=sz(1)
for i= 1:rowNum
    est = feval(fitobject5,checkX5(i,1))
    err= abs(est-checkY5(i,1))
    errSum5(i)=err
end
e5= sum(errSum5,2)



if e1<e2 & e1<e3 & e1<e4 & e1<e5
    plot(fitobject1,'g');  hold on
    plot(fitobject2, 'b--'); hold on
    plot(fitobject3,'y--'); hold on
    plot(fitobject4,'k--'); hold on
    plot(fitobject5,'m--'); hold on
    plot(xArr,yArr,'*'); hold off
end

if e2<e1 & e2<e3 & e2<e4 & e2<e5
    plot(fitobject1,'g--');  hold on
    plot(fitobject2, 'b'); hold on
    plot(fitobject3,'y--'); hold on
    plot(fitobject4,'k--'); hold on
    plot(fitobject5,'m--'); hold on
    plot(xArr,yArr,'*'); hold off
end

if e3<e1 & e3<e2 & e3<e4 & e3<e5
    plot(fitobject1,'g--');  hold on
    plot(fitobject2, 'b--'); hold on
    plot(fitobject3,'y'); hold on
    plot(fitobject4,'k--'); hold on
    plot(fitobject5,'m--'); hold on
    plot(xArr,yArr,'*'); hold off
end

if e4<e1 & e4<e3 & e4<e2 & e4<e5
    plot(fitobject1,'g--');  hold on
    plot(fitobject2, 'b--'); hold on
    plot(fitobject3,'y--'); hold on
    plot(fitobject4,'k'); hold on
    plot(fitobject5,'m--'); hold on
    plot(xArr,yArr,'*'); hold off
end

if e5<e1 & e5<e3 & e5<e2 & e5<e4
    plot(fitobject1,'g--');  hold on
    plot(fitobject2, 'b--'); hold on
    plot(fitobject3,'y--'); hold on
    plot(fitobject4,'k--'); hold on
    plot(fitobject5,'m'); hold on
    plot(xArr,yArr,'*'); hold off
end




title('Comparison of Fits against Given points')
xlabel('X Value of Point/Curve Location') 
ylabel('Y Value of Point/Curve Location')
legend('Fit 1','Fit 2','Fit 3','Fit 4','Fit 5')


