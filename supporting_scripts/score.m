%% Score
addpath(genpath(pwd));

%distances in KM
filename = 'distanceMatrixFamagusta.csv';
M = xlsread(filename);
mm=M(2:end,2:end)/1000;
cyprus.famagusta.M = mm;
cyprus.famagusta.pc = M(2:end,1);
len=length(cyprus.famagusta.pc);
dist=cyprus.famagusta.M+eye(len)*min(mm(find(mm>0)));
cyprus.famagusta.invdist2=1./dist.^2;
cyprus.famagusta.invdist2=cyprus.famagusta.invdist2/cyprus.famagusta.invdist2(1);

filename = 'distanceMatrixLarnaca.xlsx';
M = xlsread(filename);
mm=M(2:end,2:end)/1000;
cyprus.larnaca.M = mm;
cyprus.larnaca.pc = M(2:end,1);
len=length(cyprus.larnaca.pc);
dist=cyprus.larnaca.M+eye(len)*min(mm(find(mm>0)));
cyprus.larnaca.invdist2=1./dist.^2;
cyprus.larnaca.invdist2=cyprus.larnaca.invdist2/cyprus.larnaca.invdist2(1);

filename = 'distanceMatrixNicosia.csv';
M = xlsread(filename);
mm=M(2:end,2:end)/1000;
cyprus.nicosia.M = mm;
cyprus.nicosia.pc = M(2:end,1);
len=length(cyprus.nicosia.pc);
dist=cyprus.nicosia.M+eye(len)*min(mm(find(mm>0)));
cyprus.nicosia.invdist2=1./dist.^2;
cyprus.nicosia.invdist2=cyprus.nicosia.invdist2/cyprus.nicosia.invdist2(1);

filename = 'distanceMatrixPaphos.xlsx';
M = xlsread(filename);
mm=M(2:end,2:end)/1000;
cyprus.paphos.M = mm;
cyprus.paphos.pc = M(2:end,1);
len=length(cyprus.paphos.pc);
dist=cyprus.paphos.M+eye(len)*min(mm(find(mm>0)));
cyprus.paphos.invdist2=1./dist.^2;
cyprus.paphos.invdist2=cyprus.paphos.invdist2/cyprus.paphos.invdist2(1);

filename = 'distanceMatrixLimassol.xlsx';
M = xlsread(filename);
mm=M(2:end,2:end)/1000;
cyprus.limassol.M = mm;
cyprus.limassol.pc = M(2:end,1);
len=length(cyprus.limassol.pc);
dist=cyprus.limassol.M+eye(len)*min(mm(find(mm>0)));
cyprus.limassol.invdist2=1./dist.^2;
cyprus.limassol.invdist2=cyprus.limassol.invdist2/cyprus.limassol.invdist2(1);

savejson('',cyprus,'invdist.json');


