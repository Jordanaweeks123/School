[x, Fs] = audioread('testaudio.wav');
plot(x(100000:200000));
specgram(x, 1024, Fs);
sound(x, Fs);
b = [ 0.999643720498015 -1.918666629446868 0.999643720498015 ];
a = [ 1.000000000000000 -1.918666629446868 0.999287440996029 ];
y = filter(b, a, x);
sound(y,Fs);
specgram(y, 1024, Fs);