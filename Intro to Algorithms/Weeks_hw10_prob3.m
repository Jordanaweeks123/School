%Sof means similarity of and the letters are the stocks...
    %so SofAM is similarity of aapl and msft%
aapl = load('prob3_aapl.txt');
msft = load('prob3_msft.txt');
qcom = load('prob3_qcom.txt');
wfc = load('prob3_wfc.txt');
Naapl = aapl-mean(aapl(:));
Nmsft = msft-mean(msft(:));
Nqcom = qcom-mean(qcom(:));
Nwfc = wfc-mean(wfc(:));

SofAM = (Naapl'*Nmsft)/(sqrt(Naapl'*Naapl)*sqrt(Nmsft'*Nmsft));
disp('SofAM:'); 
disp(SofAM);
SofAQ = (Naapl'*Nqcom)/(sqrt(Naapl'*Naapl)*sqrt(Nqcom'*Nqcom));
disp('SofAQ:'); 
disp(SofAQ);
SofAW = (Naapl'*Nwfc)/(sqrt(Naapl'*Naapl)*sqrt(Nwfc'*Nwfc));
disp('SofAW:'); 
disp(SofAW);

figure; hold on;
plot(aapl);
plot(msft);
plot(qcom);
plot(wfc);
xlabel('other stocks');
ylabel('aapl');
legend('aapl','msft','qcom','wfc');
grid on;



