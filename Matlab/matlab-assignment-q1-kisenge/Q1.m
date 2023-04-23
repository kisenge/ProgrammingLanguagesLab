T = readtable('TriangleData.csv');

%triangle types are in solution

T(1,1)
sz= size(T)
rowNum=sz(1)



for i= 1:rowNum
    Ax=T(i,2)
    Bx=T(i,4)
    Cx=T(i,6)
    
    Ay=T(i,3)
    By=T(i,5)
    Cy=T(i,7)
    
    row= cat(2,Ax,Bx,Cx)
    col= cat(2,Ay,By,Cy)
    
    
    
    xy12= (abs(row{1,1}-row{1,2})^2)+(abs(col{1,1}-col{1,2})^2)
    xy13= (abs(row{1,1}-row{1,3})^2)+(abs(col{1,1}-col{1,3})^2)
    xy23= (abs(row{1,2}-row{1,3})^2)+(abs(col{1,2}-col{1,3})^2)
    
    len1=sqrt(xy12)
    len2=sqrt(xy13)
    len3=sqrt(xy23)
    
    %if xy12==xy13==xy23
    tol=0.0001
    
    
    if  abs(len1-len2) < tol & abs(len1-len3) < tol & abs(len2-len3) < tol
    %if isequal(len1,len2,len3)
        solution(i,1)= "Equilateral Triangle"

    elseif (abs(abs(len1^2+len2^2)-len3^2)<tol)|| (abs(abs(len1^2+len3^2)-len2^2)<tol)||(abs(abs(len2^2+len3^2)-len1^2)<tol)
        if abs(len1-len2) < tol || abs(len1-len3) < tol || abs(len2-len3) < tol
            solution(i,1)= "Right Angle Triangle Isoceles"
        elseif abs(len1-len2) > tol & abs(len1-len3) > tol & abs(len2-len3) > tol
            solution(i,1)= "Right Angle Triangle Scalene"
        else    
            solution(i,1)= "else"
        end

    elseif abs(len1-len2) > tol & abs(len1-len3) > tol & abs(len2-len3) > tol
        solution(i,1)= "Scalene Triangle"

        
    elseif (abs(len1-len2) < tol || abs(len1-len3) < tol || abs(len2-len3) < tol)&(not(abs(len1-len2) < tol & abs(len1-len3) < tol & abs(len2-len3) < tol))
        solution(i,1)= "Isosceles Triangle"
    
    %elseif (len1^2+len2^2== abs(abs(len1-len2)-len3)<tol) || (len1^2+len3^2== abs(abs(len1-len3)-len2)<tol)||(len2^2+len3^2== abs(abs(len2-len3)-len1)<tol)
    
    
    
    end
end     

count= zeros(1,5)
for i= 1:rowNum
    x=solution{i,1}

    if x=="Equilateral Triangle"
        count(1,1)= count(1,1)+1
    end

    if x=="Scalene Triangle"
        count(1,2)= count(1,2)+1
    end

    if x=="Isosceles Triangle"
        count(1,3)= count(1,3)+1
    end

    if x=="Right Angle Triangle Isoceles"
        count(1,4)= count(1,4)+1
    end

    if x=="Right Angle Triangle Scalene"
        count(1,5)= count(1,5)+1
    end



end

labels = {'Equilateral Triangle','Scalene Triangle','Isosceles Triangle','Right Angle Triangle Isoceles','Right Angle Triangle Scalene'};
pieGraph= pie(count)
p=pieGraph(4)
p.FontSize= 18
p=pieGraph(2)
p.FontSize= 18
p=pieGraph(6)
p.FontSize= 18
p=pieGraph(8)
p.FontSize= 18
p=pieGraph(10)
p.FontSize= 18
title('Distribution of Triangles')
lgd = legend(labels);
lgd.Layout.Tile = 'east';

%for i= 1:row