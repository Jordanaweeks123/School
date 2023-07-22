x1 = linspace(0, 2*pi, 3);
x2 = linspace(0, 2*pi, 7);
x3 = linspace(0, 2*pi, 21);
figure;hold on;
plot(x1, sin(x1), 'o-');
plot(x2, sin(x2), '+k-');
plot(x3, sin(x3));
xlabel('x');
ylabel('sin(x)');
title('sin(x) vs. x');
legend('sin(x1)','sin(x2)','sin(x3)');
grid on;


t1 = linspace(0, 2*pi, 21);
t2 = linspace(0, 2*pi, 201);
y1 = sin(t1)+cos(5*t1)+0.5*sin(10*t1)+1.5*cos(20*t1);
y2 = sin(t2)+cos(5*t2)+0.5*sin(10*t2)+1.5*cos(20*t2);
figure; hold on;
plot(t1, y1, 'b-');
plot(t2, y2, 'r-');
plot(t1, y1);
plot(t2, y2);
xlabel('t');
ylabel('y');
legend('y1','y2');
grid on;

