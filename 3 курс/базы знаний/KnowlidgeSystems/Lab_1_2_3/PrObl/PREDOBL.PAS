unit Predobl;

interface

uses Tipe,
  SysUtils, WinTypes, WinProcs, Messages, Classes, Graphics, Controls,
  Forms, Dialogs, StdCtrls;

type
  TFormPredObl = class(TForm)
    Label1: TLabel;
    Label2: TLabel;
    Label3: TLabel;
    Label4: TLabel;
    Edit1: TEdit;
    Label5: TLabel;
    Edit2: TEdit;
    Label6: TLabel;
    Label7: TLabel;
    Edit3: TEdit;
    Edit4: TEdit;
    Label8: TLabel;
    Label9: TLabel;
    Label10: TLabel;
    Label11: TLabel;
    Edit5: TEdit;
    Edit6: TEdit;
    Edit7: TEdit;
    Edit8: TEdit;
    Button1: TButton;
  private
    { Private declarations }
  public
    { Public declarations }
  end;

var
  FormPredObl: TFormPredObl;
 const
  eps=0.3;  a0=1; b0=10;
procedure eval_proc(number:integer; par:domen;
                    var val:string40;var KD:integer); stdcall;// export;

implementation

{$R *.DFM}
 function fff(x:real):real;
  begin fff:=sqr(x-2.5); end;
 var a,b,x1,x2:real;

 {��� ������ ���������}
procedure eval_proc(number:integer; par:domen;
 var val:string40; var KD:integer); stdcall;
 procedure initial(var a,b:real);  {��������� ���������}
 begin   val:='���������';
  a:=a0; b:=b0;
{  ShowMessage('��������� ���������');}
  FormPredObl.Show{Modal};
  FormPredObl.Edit1.Text:=FloatToStr(a0);
  FormPredObl.Edit4.Text:=FloatToStr(b0);
 end;
 procedure aa1(var x1,x2:real);  {���������}
 var x:real;
 begin   val:='���������';
{  ShowMessage('���������');}
  x:=(a+b)/2; x1:=x-eps/2; x2:=x+eps/2;
 end;
 procedure a2;  {����������}
 begin   val:='��������';
  FormPredObl.Show{Modal};
  FormPredObl.Edit1.Text:=FormatFloat('0.000',a);
  FormPredObl.Edit2.Text:=FormatFloat('0.000',x1);
  FormPredObl.Edit3.Text:=FormatFloat('0.000',x2);
  FormPredObl.Edit4.Text:=FormatFloat('0.000',b);
  FormPredObl.Edit5.Text:=FormatFloat('0.000',fff(a));
  FormPredObl.Edit6.Text:=FormatFloat('0.000',fff(x1));
  FormPredObl.Edit7.Text:=FormatFloat('0.000',fff(x2));
  FormPredObl.Edit8.Text:=FormatFloat('0.000',fff(b));
 end;
 procedure a3(a1:real; var a:real); {�������_a}
 begin
{  ShowMessage('������� �');}
    if fff(x1)>fff(x2) then a:=x1;
    if abs(a-a1)<=eps then val:='��'
    else val:='���';
 end;
 procedure a4(b1:real; var b:real);  {�������_b}
 begin
{  ShowMessage('������� �');}
    if fff(x1)<fff(x2) then b:=x2;
    if abs(b-b1)<=eps then val:='��'
    else val:='���';
 end;
 procedure a5(a,b:real;ans:string40);  {�����}
 var val1:string40;
 begin
{  ShowMessage('�����');}
  if abs(a-b)<=2*eps+eps/100 then val1:='��' else val1:='���';
  if val1=ans then val:='��' else val:='���';
 end;
 procedure a6; {����������}
 begin
ShowMessage('  � � � � � � � � � �'+#13+
'x1='+FormatFloat('0.000',x1)+
' f(x1)='+FormatFloat('0.000',fff(x1))+#13+
'x2='+FormatFloat('0.000',x2)+
' f(x2)='+FormatFloat('0.000',fff(x2)));
 end;
 begin (*eval_proc*)             {������������}
  if not FlagPrObl then
  begin
   FormPredObl:= TFormPredObl.Create(Application);
   FlagPrObl:=True;
  end;
{  if FormPredObl.ShowModal=mrOk then}
{  FormPredObl.Show;}
  val:='��'; KD:=100;            {���������   }
  case number of                 {�����       }
   3 : initial(a,b);   {��������� ���������}
   4 : aa1(x1,x2);     {���������          }
   5 : a2;             {����������         }
   6 : a3(par.dr,a);   {�������_a          }
   7 : a4(par.dr,b);   {�������_b          }
   8 : a5(a,b,par.dw); {�����              }
   9 : begin
        a6;             {����������         }
        FormPredObl.Free;
       end;
  end;
{  FormPredObl.Free;}
 end(*eval_proc*);

end.
