%change the path accordingly to where you saved the reposit


list={'Thibault_ACC_essai2.mat', '2023_05_02_Essai2.txt',
    'Thibault_ACC_essai3.mat', '2023_05_02_Essai3.txt',
    'Thibault_ACC_essai4.mat', '2023_05_02_Essai4.txt'};

    
for k=1:size(list(:,1))
    param.FileName=list{k,1};
    param.PathName='D:\git_network\vehlib\Users\Thibault\Measurements';
    param.syncVoies='Cons_startCycle_L';
    param.SousEch=10;
    [Struct, ERR]=lectureMatFile4Vehlib(param);
    
    param2.FileName=list{k,2};
    param2.PathName='D:\git_network\vehlib\Users\Thibault\Measurements';
    param2.syncVoies='TOP_CVS_NN';
    [ERR,Struct,rcd]=lecture_rcd2XMLFormat(param2,Struct)
    
    
    affectVehlibStruct2Workspace(Struct,'caller');
    
    
    %Temps, vit, vit_dem, debit, rapport,
    temps = 1:0.1:min(Temps_RCD(end),Time_dsp(end));
    vit_rcd = interp1(Time_dsp,vit_veh,temps);
    vit_dem_rcd = interp1(Time_dsp,vitdem_cin,temps);
    rappvit_rcd = interp1(Time_dsp,rappvit_bv_L,temps);
    FB_RATE_cor = interp1(Temps_RCD,FB_RATE,temps);
    FB_DENS_cor = interp1(Temps_RCD,FB_DENS,temps);
    [~, filename_wo_ext, ~]=fileparts(param2.FileName);
    
    filename=[filename_wo_ext,'.csv'];
    
    fid = fopen(filename,'w');
    for i = 1:length(temps)
        fprintf(fid,'%.1f %.1f %.1f %.1f %.2f %.2f\n',temps(i),vit_rcd(i),vit_dem_rcd(i),rappvit_rcd(i), ...
            FB_RATE_cor(i),FB_DENS_cor(i));
    end
    fclose(fid);
    
    filename=[filename_wo_ext,'.xml'];
    pathname='D:\git_network\vehlib\Users\Thibault\Measurements';
    ecritureXMLFile4Vehlib(Struct,filename,pathname);
end

%explgr(Struct)