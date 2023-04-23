clear 


[A,delimiterOut,headerlinesOut] = importdata("iris.data") 


iris = importdata('iris.data',delimiterOut);

lenA=size(iris)
rowNum=lenA(1,1)
%cleanerIris= zeros(1,1)

for i= 1:rowNum
    new= split(iris{i,1},delimiterOut,2)
    %row= cell2mat(new)
    cleanerIris(i,:)=new

end

testingRandom= round(rand(5,1)*150)
trainingSet= cleanerIris
trainingSetIndex= 1:1:150
trainingSetIndex= reshape(trainingSetIndex,[150,1])

for i=1:5
    x=testingRandom(i,1)
    row=cleanerIris(x,:)%multiple vals
    trainingSet(x,:)= []
    trainingSetIndex(x,:)= []
    testSet(i,:)=row
end







tstSet= knn5(trainingSet,trainingSetIndex,testSet)
fprintf("\n\nThe list of indexes of training points:")
trainingSetIndex
    %for i=1:145
        %disp(trainingSetIndex(i,1))
    %end
fprintf("\nPlease scroll up for solutions")


function [tstSet]= knn5(trainingSet,trainingSetIndex,testSet)
    tstSet= zeros(5,5);
    trnSet= zeros(145,5);
    
    %tst
    for q=1:5
        classNumber= strings;
        for k=1:4
            tstSet(q,k)=str2double(testSet{q,k});     
        end
        
         %if trainingSet{j,5}=="Iris-setosa"
        if strcmp(testSet{q,5},"Iris-setosa");
            tstSet(q,5)=1;
        
        elseif strcmp(testSet{q,5},"Iris-versicolor");
        %elseif trainingSet{j,5}=='Iris-versicolor'
            tstSet(q,5)=2;
        
        else strcmp(testSet{q,5},"Iris-virginica");
        %else trainingSet{j,5}=="Iris-virginica"
            tstSet(q,5)=3;
        end

        


        %training
        for j=1:145
            for k=1:4
                trnSet(j,k)=str2double(trainingSet{j,k});
            end
    
            %if trainingSet{j,5}=="Iris-setosa"
            if strcmp(trainingSet{j,5},"Iris-setosa");
                trnSet(j,5)=1;
            
            elseif strcmp(trainingSet{j,5},"Iris-versicolor");
            %elseif trainingSet{j,5}=='Iris-versicolor'
                trnSet(j,5)=2;
            
            else strcmp(trainingSet{j,5},"Iris-virginica");
            %else trainingSet{j,5}=="Iris-virginica"
                trnSet(j,5)=3;
            end
    
            
        end
    
        %distances= sqrt(sum((trnSet - testSet(i,:)).^2, 2))
        %predict=distances
        
    
        distances= zeros(145,5);
    
        for testI=1:1
            for j=1:145
                for k=1:4
                    ts1=trnSet(j,k);
                    ts2=tstSet(q,k);
    
                    distances(j,k)= sqrt(sum((ts1 - ts2).^2, 2));
                end
                
            end
        end
    
    
        distSum= zeros(145,5);
        for i=1:145
            dSum= sum(distances,2);
    
        end
    
        min5Index= zeros(5,1);
        for i=1:5
            [minVal,minIndex]=min(dSum);
            dSum(minIndex,:)=[];
            min5Index(i,1)=minIndex;
        end
    %     distances= sqrt(sum((trnSet - tstSet).^2, 2))
        %for i=1:
    
        %classNumber= zeros(5,1)
        for i=1:5
            in=min5Index(i,1);
            
            if trnSet(in,5)==1;
                classNumber(i,1)="Iris-setosa";
    
            elseif trnSet(in,5)==2;
                classNumber(i,1)="Iris-versicolor";
    
            elseif trnSet(in,5)==3;
                classNumber(i,1)="Iris-virginica";
            end
            
        end

       
    
        prediction1= mode(categorical(classNumber));
        %p1=categorical(classNumber)
        p1=categories(prediction1);
        prediction=p1{1,1};

        actual1= tstSet(q,5);
        actual=string;
        if actual1==1;
            actual="Iris-setosa";
    
        elseif actual1==2;
            actual="Iris-versicolor";
    
        elseif actual1==3;
            actual="Iris-virginica";
        end
    
    %     actual(i,1)=tst(,5)
    % 
    %     for i=1:5
    %         
    %         if min5Index(i,1)==1
    %             classNumber(i,1)="Iris-setosa"
    % 
    %         elseif min5Index(i,1)==2
    %             classNumber(i,1)="Iris-versicolor"
    % 
    %         else
    %             classNumber(i,1)="Iris-virginica"
    %         end
    %     end
    % 
        fprintf("Trial:"+q)

        fprintf("\nSub predictions are:")
        classNumber

        fprintf("\nThe prediction is:")
        disp(prediction)
        
        fprintf("The actual is:")
        disp(actual)

        if strcmp(prediction,actual);
            fprintf("The prediction was correct.\n\n\n")
        else
            fprintf("The prediction was incorrect.\n\n\n")
        end
    end

    
end

