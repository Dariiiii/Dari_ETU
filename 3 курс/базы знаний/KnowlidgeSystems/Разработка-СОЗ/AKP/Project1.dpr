program Project1;

uses
  Forms,
  frmtest in 'frmtest.pas' {frmTestLog},
  frmtestwait in 'frmtestwait.pas' {frmWait},
  Predobl in 'dichotomy\PrObl\PREDOBL.PAS' {FormPredObl},
  Tipe in 'dichotomy\PrObl\TIPE.PAS';

{$R *.res}

begin
  Application.Initialize;
  Application.CreateForm(TFormPredObl, FormPredObl);
  Application.CreateForm(TfrmTestLog, frmTestLog);
  Application.CreateForm(TfrmWait, frmWait);
//  Application.CreateForm(TFormPredObl, FormPredObl);
  Application.Run;
end.
