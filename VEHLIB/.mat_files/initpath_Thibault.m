%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%            nom         : initpath.m
%
%            auteur      : INRETS/LTE
% 
%       Date de creation : janvier 99
%
%            Sujet       : initialisation des paths matlab pour les modeles
%                          de simulation de la bibliotheque VEHLIB
%                          Ici, Paths utilisateurs
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


% variable path

currentdir=pwd;

vehlibListDir={ fullfile(currentdir, 'Utilities')
                fullfile(currentdir, 'Utilities', 'Main')
                fullfile(currentdir, 'Utilities', 'Main', 'Forward')
};

cellfun(@(x) addpath(x), vehlibListDir);
% clear workspace variables
clear currentdir;

