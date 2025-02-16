function fitMultifileAvgMeasData2Benchmarking(UseNoIntFromOtherFile)
% Select multiple RB 1D sweeps for input. This script averages them and fit
% them to find gate fidelity. Error bars will be shown 
%
%UseNoIntFromOtherFile variable can be used if you want to use no_interleaved
%data from previous set but interleaved data from current set. Put 1 for
%dissipator OFF data and 2 for dissipator ON data if you want to use old
%interleavd numbers for depolarising parameters. Leave it empty if you just
%want to use normal RB data.

% Select files to plot.
[filenames, pathnames, status] = selectMeasurementDataFile;
if ~status
    return
end

if ~iscell(filenames)
    filenames = {filenames};
end
if ~iscell(pathnames)
    pathnames = {pathnames};
end


% Read the data file, convert the variable names, and specify the units.
try
    data = cell(0);
    for k = 1:length(filenames)
        file = fullfile(pathnames{k}, filenames{k});
        data{k} = processMeasurementData(importMeasurementData(file));
    end
catch
    error('The selected files contain unmatched data.')
end

% Check loaded data for possibility of generating errorbars
if isfield(data{1}, 'Interleaved_Probabilities')
    errors = 0;
else
    errors = 0;
end

% if exist('errorss','var')
% errors = errorss;
% end


for k = 1:length(filenames)
    No_Int_Probability_TempData(k,:) = data{k}.No_Interleaved_Probability;
    Int_Probability_TempData(k,:) = data{k}.Interleaved_Probability;
    No_Int_probabilities_TempData(k,:,:) = data{k}.No_Interleaved_Probabilities;    
    Int_probabilities_TempData(k,:,:) = data{k}.Interleaved_Probabilities;
end

AvgData.No_Interleaved_Probability = mean(No_Int_Probability_TempData,1);
AvgData.Interleaved_Probability = mean(Int_Probability_TempData,1);
AvgData.No_Interleaved_Probabilities = mean(No_Int_probabilities_TempData,1);
AvgData.Interleaved_Probabilities = mean(Int_probabilities_TempData,1);

% for fn = fieldnames(data{1})'
%    AvgData.(fn{1}) = data{1}.(fn{1});
% end

dep_rels = data{1}.rels.Interleaved_Probability;

% Analyze and plot 1D data
if length(dep_rels) == 1
    %Find P1 for Interleaved and no interleave for each number of Cliffords
    p1_array = zeros(length(data{1}.Number_of_Cliffords), 3);%NoInter, Inter, NoC
    p1_array(:,1) = 1 - AvgData.No_Interleaved_Probability;
    p1_array(:,2) = 1 - AvgData.Interleaved_Probability;
    p1_array(:,3) = data{1}.Number_of_Cliffords;
    
    % Fit the two curves for depolarizing parameter
    
    [out.no_int_x, out.no_int_y]=prepareCurveData(p1_array(:,3), p1_array(:,1));
    [out.fr_No_Interleave, ~] = fidelityFit(out.no_int_x, out.no_int_y);
    
    [out.int_x, out.int_y]=prepareCurveData(p1_array(:,3), p1_array(:,2));
    [out.fr_Interleave, ~] = fidelityFit(out.int_x, out.int_y);
    
    r_c_est = 0.5*(1-out.fr_Interleave.b/out.fr_No_Interleave.b);
    out.fidelity_gate = 1 - r_c_est;
    
    fr_i_conf = confint(out.fr_Interleave, 0.6827);
    fr_no_conf = confint(out.fr_No_Interleave, 0.6827);
    
    std_i_b = (fr_i_conf(2,2) - fr_i_conf(1,2))/2;
    std_no_b = (fr_no_conf(2,2) - fr_no_conf(1,2))/2;
    
    term1 = std_i_b/out.fr_No_Interleave.b;
    term2 = out.fr_Interleave.b/out.fr_No_Interleave.b^2 * std_no_b;
    out.sigma_r_c_est = 0.5 * sqrt(term1^2 + term2^2);

    
    %In case you want to use the same P and deltaP as extracted from
    %previous measurements, you could place them in place of 0.97568 and
    %0.001063
    if exist('UseNoIntFromOtherFile', 'var')
        if UseNoIntFromOtherFile == 1
            b_for_Interleave_forjustInt = 0.98724;
            std_no_b_forjustInt = 0.0014117;
        else
            b_for_Interleave_forjustInt = 0.97568;
            std_no_b_forjustInt = 0.001063;
        end 
        r_c_est_forjustInt = 0.5*(1-out.fr_Interleave.b/b_for_Interleave_forjustInt);
        fidelity_gate_forjustInt = 1 - r_c_est_forjustInt;
        term1_forJustInt = std_i_b/b_for_Interleave_forjustInt;
        term2_forJustInt = out.fr_Interleave.b/b_for_Interleave_forjustInt^2 * std_no_b_forjustInt;
        sigma_r_c_est_justforInt = 0.5 * sqrt(term1_forJustInt^2 + term2_forJustInt^2);
    end

    
    % Plotting
    createFigure; hold on;
    
    %plot data with or without errorbars based on whether or not the datafile
    % contains the required information

    if errors
        out.no_int_std = std(AvgData.No_Interleaved_Probabilities,1,2);
        out.int_std = std(AvgData.Interleaved_Probabilities,1,2);
        plotErrorbar(out.no_int_x,out.no_int_y,out.no_int_std);
        plotErrorbar(out.int_x,out.int_y,out.int_std);
    else
        plotSimple(out.no_int_x,out.no_int_y);
        plotSimple(out.int_x,out.int_y);
    end
    
    %plot the fits on top of the data
    
    ax=gca;
    ax.ColorOrderIndex=1;
    plotSimple(out.no_int_x,...
        out.fr_No_Interleave(out.no_int_x),'-');
    plotSimple(out.int_x,...
        out.fr_Interleave(out.int_x),'-');
    
    [~,filename,ext] = fileparts(data{1}.Filename);
    filename=strrep(filename,'_','\_');
    fid_str = [data{1}.Interleaving_Gate,'Gate Fidelity: ',...
        num2str(out.fidelity_gate),'\pm',num2str(out.sigma_r_c_est)];
    if exist('UseNoIntFromOtherFile', 'var')
        fid_str_forjustInt = [data{1}.Interleaving_Gate,'Gate Fidelity\_forJustInt: ',...
            num2str(fidelity_gate_forjustInt),'\pm',num2str(sigma_r_c_est_justforInt)];
    end
    dep_pars = [' P = ', num2str(out.fr_No_Interleave.b),'  ','\Delta P = ', num2str(std_no_b),'  ',' P_C = ', num2str(out.fr_Interleave.b),'  ','\Delta P_C = ', num2str(std_i_b)];
%     title(title_str_cell, 'FontSize', 10)
    
    if exist('UseNoIntFromOtherFile', 'var')
        title({[strrep(filenames{1}, '_', '\_'), ' - ',...
        strrep(filenames{end}, '_', '\_'),': ',data{1}.Timestamp],...
            fid_str, fid_str_forjustInt, dep_pars});
    else
        title({[strrep(filenames{1}, '_', '\_'), ' - ',...
        strrep(filenames{end}, '_', '\_'),': ',data{1}.Timestamp],...
            fid_str, dep_pars}); 
    end 

    xlabel('Number of Cliffords')
    ylabel('Sequence Fidelity')
    leg=legend('Interleaved Gate: None',...
        ['Interleaved Gate: ',data{1}.Interleaving_Gate]);
    set(leg,'Location','best')
    
end
end

function [fitresult, gof] = fidelityFit(xData, yData)

% Set up fittype and options.
ft = fittype( 'a*b^x + c', 'independent', 'x', 'dependent', 'y' );
opts = fitoptions( 'Method', 'NonlinearLeastSquares',...
                    'Robust', 'LAR',...
                      'MaxFunEvals',10000,...
                      'MaxIter',10000,...
                      'Algorithm','Trust-Region');
opts.Display = 'Off';
opts.Lower = [0, 0, 0];
opts.StartPoint = [0.4 0.9 mean(yData)];

% Fit model to data.
[fitresult, gof] = fit( xData, yData, ft, opts );

end