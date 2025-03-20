unit frmtestwait;

interface

uses
  Windows, Messages, SysUtils, Variants, Classes, Graphics, Controls, Forms,
  Dialogs, StdCtrls, ExtCtrls;

Const WAIT_MODE_1 = 1;
      WAIT_MODE_2 = 2;

type
  TfrmWait = class(TForm)
    Label1: TLabel;
    btnOK: TButton;
    Panel1: TPanel;
    Panel2: TPanel;
    btnYes: TButton;
    MR_NO: TButton;
    procedure btnOKClick(Sender: TObject);
    procedure FormShow(Sender: TObject);
    procedure btnYesClick(Sender: TObject);
    procedure MR_NOClick(Sender: TObject);
  private
  public
    clicked:Integer;
  end;

var
  frmWait: TfrmWait;

 Procedure ShowWait(text:String; mode:INteger);
implementation



{$R *.dfm}

procedure TfrmWait.btnOKClick(Sender: TObject);
begin
 Clicked := ID_OK;
 hide;
end;

procedure TfrmWait.FormShow(Sender: TObject);
begin
 Clicked := 0;
end;

Procedure ShowWait(text:String; mode:INteger);
begin
 if frmWait=nil then
   Application.CreateForm(TfrmWait, frmWait);
 frmWait.label1.caption := text;
 case Mode of
   WAIT_MODE_1: begin frmWait.Panel1.Show; frmWait.Panel2.Hide; end;
   WAIT_MODE_2: begin frmWait.Panel1.Hide; frmWait.Panel2.Show; end;
 end;
 frmWait.Show;
end;

procedure TfrmWait.btnYesClick(Sender: TObject);
begin
   Clicked := ID_YES; hide;
end;

procedure TfrmWait.MR_NOClick(Sender: TObject);
begin
   Clicked := ID_NO; hide;
end;

end.
