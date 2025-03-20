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

 {АОС методу дихотомии}
procedure eval_proc(number:integer; par:domen;
 var val:string40; var KD:integer); stdcall;
 procedure initial(var a,b:real);  {начальная установка}
 begin   val:='проведена';
  a:=a0; b:=b0;
{  ShowMessage('НАЧАЛЬНАЯ УСТАНОВКА');}
  FormPredObl.Show{Modal};
  FormPredObl.Edit1.Text:=FloatToStr(a0);
  FormPredObl.Edit4.Text:=FloatToStr(b0);
 end;
 procedure aa1(var x1,x2:real);  {дихотомия}
 var x:real;
 begin   val:='проведена';
{  ShowMessage('ДИХОТОМИЯ');}
  x:=(a+b)/2; x1:=x-eps/2; x2:=x+eps/2;
 end;
 procedure a2;  {информация}
 begin   val:='выведена';
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
 procedure a3(a1:real; var a:real); {граница_a}
 begin
{  ShowMessage('ГРАНИЦА А');}
    if fff(x1)>fff(x2) then a:=x1;
    if abs(a-a1)<=eps then val:='да'
    else val:='нет';
 end;
 procedure a4(b1:real; var b:real);  {граница_b}
 begin
{  ShowMessage('ГРАНИЦА В');}
    if fff(x1)<fff(x2) then b:=x2;
    if abs(b-b1)<=eps then val:='да'
    else val:='нет';
 end;
 procedure a5(a,b:real;ans:string40);  {конец}
 var val1:string40;
 begin
{  ShowMessage('КОНЕЦ');}
  if abs(a-b)<=2*eps+eps/100 then val1:='да' else val1:='нет';
  if val1=ans then val:='да' else val:='нет';
 end;
 procedure a6; {результаты}
 begin
ShowMessage('  Р Е З У Л Ь Т А Т Ы'+#13+
'x1='+FormatFloat('0.000',x1)+
' f(x1)='+FormatFloat('0.000',fff(x1))+#13+
'x2='+FormatFloat('0.000',x2)+
' f(x2)='+FormatFloat('0.000',fff(x2)));
 end;
 begin (*eval_proc*)             {обязательная}
  if not FlagPrObl then
  begin
   FormPredObl:= TFormPredObl.Create(Application);
   FlagPrObl:=True;
  end;
{  if FormPredObl.ShowModal=mrOk then}
{  FormPredObl.Show;}
  val:='да'; KD:=100;            {системная   }
  case number of                 {часть       }
   3 : initial(a,b);   {начальная установка}
   4 : aa1(x1,x2);     {дихотомия          }
   5 : a2;             {информация         }
   6 : a3(par.dr,a);   {граница_a          }
   7 : a4(par.dr,b);   {граница_b          }
   8 : a5(a,b,par.dw); {конец              }
   9 : begin
        a6;             {результаты         }
        FormPredObl.Free;
       end;
  end;
{  FormPredObl.Free;}
 end(*eval_proc*);

end.
