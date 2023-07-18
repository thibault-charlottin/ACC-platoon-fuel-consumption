path_directory='/Users/thibault.charlottin/LICIT_LAB Dropbox/Thibault Charlottin/Banc moteur/individual_trajectories/'; 
out_path = '/Users/thibault.charlottin/LICIT_LAB Dropbox/Thibault Charlottin/Banc moteur/Vehlib_results/';
%change the path accordingly to where you saved the reposit
original_files=dir([path_directory '/*.csv']); 
vehicle = 'Renault_Kadjar_TCE130';
%vehicle = 'Renault_Kadjar_TCE130_CONTROL';
architecture = 'rappvit_bv';
for k=1:length(original_files)
    filename=[path_directory '/' original_files(k).name];
    if contains(filename, '_14_5ms') 
        M = readmatrix(filename);
        t = M(2:end,2);
        v = M(2:end,3);
        CYCL.ntypcin = 1 ;
        CYCL.recharge = 0; % Recharge
        CYCL.temps = 0:1:max(t);
        CYCL.tmax = max(CYCL.temps);
        CYCL.vitesse = interp1(t,v,CYCL.temps);
        CYCL.pente = 0;
        VD.CYCL = CYCL;
        [err, vehlib, VD]=ini_calcul(vehlib, VD);
        sim(vehlib.simulink);
        results = [tsim vit*3.6 acc*3.6 distance cmt.*wmt/1000 dcarb];
        emissions = [cocum hccum noxcum];
        emissions = emissions';
        writematrix(results,[out_path '/consumption/' original_files(k).name]); 
        writematrix(emissions,[out_path,'/emissions/' original_files(k).name]);
    end
end