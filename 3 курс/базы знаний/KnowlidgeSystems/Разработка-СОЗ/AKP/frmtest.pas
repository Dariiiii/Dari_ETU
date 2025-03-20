unit frmtest;
//������������ APK_dichotomy
interface

uses
  ShellAPI,Windows, Messages, SysUtils, Variants, Classes, Graphics, Controls, Forms,
  Dialogs, StdCtrls, ExtCtrls, Grids, Menus, ActnList, db{, MathStat, MMSystem, approx};
type
  TfrmTestLog = class(TForm)
    Grid: TStringGrid;
    Panel1: TPanel;
    btnClose: TButton;
    Timer1: TTimer;
    MainMenu1: TMainMenu;
    N1: TMenuItem;
    N2: TMenuItem;
    N3: TMenuItem;
    ActionList1: TActionList;
    actTesting_CurrentTask: TAction;
    actTesting_AllTasks: TAction;
    N4: TMenuItem;
    miAskBegin: TMenuItem;
    miTestWait: TMenuItem;
    Timer2: TTimer;
    N5: TMenuItem;
    procedure FormCreate(Sender: TObject);
    procedure GridDrawCell(Sender: TObject; ACol, ARow: Integer;
      Rect: TRect; State: TGridDrawState);
    procedure btnCloseClick(Sender: TObject);
    procedure FormResize(Sender: TObject);
    procedure GridSelectCell(Sender: TObject; ACol, ARow: Integer;
      var CanSelect: Boolean);
    procedure GridDblClick(Sender: TObject);
    procedure GridKeyPress(Sender: TObject; var Key: Char);
    procedure Timer1Timer(Sender: TObject);
    procedure actTesting_CurrentTaskExecute(Sender: TObject);
    procedure miAskBeginClick(Sender: TObject);
    procedure actTesting_AllTasksExecute(Sender: TObject);
    procedure Timer2Timer(Sender: TObject);
    procedure N5Click(Sender: TObject);
  private
    destx,desty:Integer;
    hw:THintWindow;
    procedure InitHint(text:String);
    procedure MoveHint;

    procedure InitGrid;
    procedure ResizeGrid;
    procedure FillTaskNames;
    procedure FillRes;
    procedure BeginTest(task_n:INteger);
    procedure SetResult(task_n, res_id:Integer);
  public
    procedure ShowHintAnim(dx,dy:Integer; fname:String);
  end;

var
  frmTestLog: TfrmTestLog;
  TestFlag:Boolean = false;
  AutoTest:Boolean = false;
  TestStop:boolean = false;

type PMyEventHandler = procedure (Sender: TObject) of object;

implementation

uses frmtestwait, Predobl, Tipe;

{$R *.dfm}

var WorkDir,
    SampleDir,
    ResultDir,
    EtalonDir:String;

Type TTestProc = function:Integer;

Const TaskCount = 6{19};

      trNoTest  = 1;
      trGood    = 2;
      trEtalon  = 3;
      trRuntime = 4;
      trExpert = 5;
      trFiles = 6;

Var TaskNames:Array [1..TaskCount]of String = (
'������� ������ ���������',
'��������� ��������� � ���������',
'������� �',
'������� �',
'�������� ���������',
'2.1 ������ (��� ��� �1)'  
);

Results:Array[1..6] of String = (
'�� �������������',
'�������',
'����������� � ��������',
'������ ����������',
'����������� ���������',
'���������� ��');

Message1:PChar ='�������� ������ � ��������� ������.'+#13#10+
                          '������� OK ��� ������ �������...';
Message2:PChar ='���������������� ������ ��������.'+#13#10+
                '������� "��" ��� ��������� � ��������.';

procedure TestMessage(text:String);
begin
 if frmTestLog.miTestWait.Checked then
 begin
//  Application.MessageBox(PChar(text), '���������', MB_OK);
  ShowWait(text, WAIT_MODE_1);

  Repeat
   Application.ProcessMessages;
  Until frmWait.Clicked > 0;
 end;
end;

function TestMessage2(text:String):integer;
begin
 if frmTestLog.miTestWait.Checked then
 begin
//  Application.MessageBox(PChar(text), '���������', MB_OK);
  ShowWait(text, WAIT_MODE_2);

  while true do begin
    Application.ProcessMessages;
    Result := frmWait.Clicked;
    if Result > 0 then Break;
  end;
 end;
end;

function LookInList(lst:TStrings; what:string):integer;
var i:integer;
begin
   Result := -1;
   what := UpperCase(what);
   i := 0;
   while (i < lst.Count) and (pos(what, UpperCase(lst[i])) = 0) do inc(i);
   if i < lst.Count then Result := i;
end;

{===========================������ ���� ������=====================================}
{===========================4_1_1=====================================}
function Test4_1_1:Integer;
var mtit:string;
// var a,b,x1,x2:real;
var ans2:string40;
label 1;
begin
  mtit:='������� ������ ���������';
  Result := trGood;
  try
    testmessage('������� �� ��� ������� ' + mtit);
     testmessage('����� ��������� ��������� ��������� ');
     initial(a,b);   {��������� ���������}
   testmessage('����� ��������� ��������� ');
   aa1(x1,x2);   {���������}
   testmessage('����� ����������� ���������� ');
   a2;  {����������}
  1: testmessage(' ����������� �������_a.'+#10#13+
  ' ������� �������� a (real). '+#10#13+
  ' ��������� �������_� :::  if  f(x1)>f(x2) then a:=x1');
   a3(a);   {�������_a}
   testmessage('����� ����������� ���������� ');
   a2;   {����������}
   testmessage('����������� �������_b. '+#10#13+
   '������� �������� b (real)'+#10#13+
   ' ��������� �������_� :::  if  f(x1)<f(x2) then b:=x2');
   a4(b);    {�������_b}
   testmessage('����� ����������� ���������� ');
   a2;  {����������}
   testmessage('����� ��������� ��������� ');
   aa1(x1,x2);   {���������}
   testmessage('����� ����������� ���������� ');
   a2;   {����������}
   testmessage('�������� ���������'+#10#13+
   ' �������� ����������? (��/���) '+#10#13+
   '��������� ����� :::  if abs(a-b)<= 2*eps+eps/100 then �� else ���');

  if TestMessage2('���� �������� ���������� (if abs(a-b)<= 2*eps+eps/100 then �� else ���),'+#10#13+
               '���� ��� ���, �� ������� "��" ����� "���".') = ID_YES then
     begin
         a5(a,b,ans2);        {�����}
         if (ans2 = '��') then       testmessage('����� �������. '+#10#13+
                                    '�������� ����������? (��/���)'+#10#13+
          ' ��������� ����� :::  if abs(a-b)<= 2*eps+eps/100 then �� else ���')
          else  begin testmessage('�� ����� ��������'); Result := trEtalon; end;
     end else
     begin
       a5(a,b,ans2);      {�����}
       if (ans2 <> '��') then begin testmessage('�������� �� ���������� ');goto 1; end
                         else begin testmessage('�� ��������'); Result := trExpert; end;
     end;
   a6;    {����������}
  except
     Result := trRuntime;
  end;
end;


{===========================4_1_2=====================================}
function Test4_1_2:Integer;
var mtit:string;
begin
  mtit:='��������� ��������� � ���������';
  Result := trGood;
  try
      testmessage('������� �� ��� ������� ' + mtit);
     initial(a,b);   {��������� ���������}
     testmessage('��������� ��������� ');
   aa1(x1,x2);         {���������}
   testmessage('��������� ');
   a2;       {����������}
  except
     Result := trRuntime;
  end;
end;


{===========================4_1_3=====================================}
function Test4_1_3:Integer;
var mtit:string;
begin
  mtit:='������� �';
  Result := trGood;
  try
      testmessage('������� �� ��� ������� ' + mtit);
     initial(a,b);   {��������� ���������}
     testmessage('��������� ��������� ');
   aa1(x1,x2);     {���������}
   testmessage('��������� ');
   a2;      {����������}
   a3(a);    {�������_a}
   testmessage('�������_a ');
   a2;      {����������}
   testmessage('�����������_���������� ');
  except
     Result := trRuntime;
  end;
end;


{===========================4_1_4=====================================}
function Test4_1_4:Integer;
var mtit:string;
begin
  mtit:='������� �';
  Result := trGood;
  try
      testmessage('������� �� ��� ������� ' + mtit);
     initial(a,b);   {��������� ���������}
     testmessage('��������� ��������� ');
   aa1(x1,x2);      {���������}
   testmessage('��������� ');
   a2;  {����������}
   a3(a);     {�������_a}
   testmessage('�������_a ');
    a2;   {����������}
   testmessage('�����������_���������� ');
   a4(b);    {�������_b}
   testmessage('�������_b ');
   a2;  {����������}
   testmessage('�����������_���������� ');
  except
     Result := trRuntime;
  end;
end;

{===========================4_1_5=====================================}
function Test4_1_5:Integer;
var mtit:string;
ans, ans2:string40;
begin
  mtit:='�������� ���������';
  Result := trNoTest;
  try
    testmessage('������� �� ��� ������� ' + mtit);
     testmessage('����� ��������� ��������� ��������� ');
     initial(a,b);   {��������� ���������}
   testmessage('����� ��������� ��������� ');
   aa1(x1,x2);     {���������}
   testmessage('����� ����������� ���������� ');
   a2;   {����������}
 { 1:} testmessage(' ����������� �������_a.'+#10#13+
  ' ������� �������� a (real). '+#10#13+
  ' ��������� �������_� :::  if  f(x1)>f(x2) then a:=x1');
   a3(a);     {�������_a}
   testmessage('����� ����������� ���������� ');
   a2;     {����������}
   testmessage('����������� �������_b. '+#10#13+
   '������� �������� b (real)'+#10#13+
   ' ��������� �������_� :::  if  f(x1)<f(x2) then b:=x2');
   a4(b);        {�������_b}
   testmessage('����� ����������� ���������� ');
   a2;    {����������}
   testmessage('����� ��������� ��������� ');
   aa1(x1,x2);   {���������}
   testmessage('����� ����������� ���������� ');
   a2;      {����������}
   testmessage('�������� ���������'+#10#13+
   ' �������� ����������? (��/���) '+#10#13+
   '��������� ����� :::  if abs(a-b)<= 2*eps+eps/100 then �� else ���');

   a5(a,b,ans2);     {�����}
  if TestMessage2('���� �������� ���������� (if abs(a-b)<= 2*eps+eps/100 then �� else ���),'+#10#13+
               '���� ��� ���, �� ������� "��" ����� "���".') = ID_YES then
   begin   ans:= '��'; if ans = ans2 then  Result := trGood else Result := trExpert; end else
   begin   ans:= '���'; if ans = ans2 then  Result := trGood else Result := trExpert; end;
   if (ans2 <> '��') then begin testmessage('�������� �� ���������� ');{goto 1;} end;
  except
     Result := trRuntime;
  end;
end;

{===========================4_2_1=====================================}
function Test4_2_1:Integer;
var mpage,mtype,mfile,mtit:string;
begin
  mpage:='2269';
  mtype:='T2';
  mfile:='A13_W2_69';
  mtit:='������ (��� ��� �1)';
  Result := trNoTest;
  try
    testmessage('������� �� ��� ������� ' + mtit);
  except
     Result := trRuntime;
  end;
end;

{===========================����� ���� ������=====================================}

function NoTest:Integer;
begin
 Application.MessageBox('������ ��� ���� ������ �� ��������!', '���������',
             MB_OK or MB_ICONWARNING);
 Result := trNoTest;
end;

Var Testers:Array[1..TaskCount] OF Pointer = (
@Test4_1_1,
@Test4_1_2,
@Test4_1_3,
@Test4_1_4,
@Test4_1_5,
@Test4_2_1
);

procedure TfrmTestLog.InitGrid;
begin
 with Grid do begin
  ColCount := 2;
  RowCount := TaskCount+1;
  FixedCols := 0;
 end;
end;

procedure TfrmTestLog.ResizeGrid;
begin
 With Grid do begin
  ColWidths[0] := 80 * ClientWidth  div 100;
  ColWidths[1] := 20 * ClientWidth div 100;
  FixedCols := 0;
  Cells[0,0] := '�������� ������';
  Cells[1,0] := '���������';
 end;
end;

procedure TfrmTestLog.FillTaskNames;
var i:integer;
begin
 with Grid do begin
  for i:=1 to TaskCount do
   Cells[0,i] := TaskNames[i];
 end;
end;

procedure TfrmTestLog.FillRes;
var i:integer;
begin
 with Grid do begin
  for i:=1 to TaskCount do
   Cells[1,i] := Results[trNoTest];
 end;
end;

procedure TfrmTestLog.FormCreate(Sender: TObject);
begin
 InitGrid;
 ResizeGrid;
 FillTaskNames;
 FillRes;
end;

procedure TfrmTestLog.GridDrawCell(Sender: TObject; ACol, ARow: Integer;
  Rect: TRect; State: TGridDrawState);
var px, py:Integer;
begin
 with TStringGrid(Sender), TStringGrid(Sender).Canvas do begin
  Font.Color := clBlack;
  py := (Rect.Top+Rect.Bottom-TextHeight(Cells[ACol,ARow])) shr 1;
  if ARow = 0 then begin
    px := (Rect.Right + Rect.Left - TextWidth(Cells[ACol,ARow])) shr 1;
    Brush.Color := clBtnFace;
  end else
  if ACol = 0 then begin
    px := Rect.Left + 4;
    Brush.Color := clCream;
  end else
  begin
   px := Rect.Left+5;
   if Cells[ACol,ARow] = Results[trNoTest] then
         Brush.Color := clWindow
   else
   if Cells[ACol,ARow] = Results[trGood] then
         Brush.Color := clLime
   else
   if Cells[ACol,ARow] = Results[trEtalon] then
         Brush.Color := clYellow
   else
   if Cells[ACol,ARow] = Results[trExpert] then
         Brush.Color := clYellow
   else
         Brush.Color := clRed;
  end;
  If gdSelected in State then begin
   Brush.Color := RGB(230,240,250);
  end;
  Pen.Color := Brush.Color;
  Rectangle(Rect);
  TextOut(px,py,Cells[ACol,ARow]);
  Pen.Color := clBtnFace;
 end;
end;


procedure TfrmTestLog.btnCloseClick(Sender: TObject);
begin
 Close;
end;

procedure TfrmTestLog.FormResize(Sender: TObject);
begin
 ResizeGrid;
 btnClose.Left := Panel1.ClientWidth - btnClose.Width - 8;
end;

procedure TfrmTestLog.GridSelectCell(Sender: TObject; ACol, ARow: Integer;
  var CanSelect: Boolean);
begin
 CanSelect := (ACol=0) and (ARow>0);
end;

procedure TfrmTestLog.BeginTest(task_n:INteger);
Var mytest:TTestProc;
begin
 if not miAskBegin.Checked or
   (Application.MessageBox(PChar('���������� � ������������:'+#10#13+
                           TaskNames[task_n]),
                           '������������',
                           MB_YESNO Or MB_ICONQUESTION)=IDYES)
 then begin
   hide;
{   Info('������ ��������������� ������������: "'+TaskNames[task_n]+'"');}
   mytest := Testers[task_n];
   SetResult(task_n, mytest());
{   Info('�������� ������ ��������. ���������: '+Grid.Cells[1, task_n]);}
   show;
  end;
end;


procedure TfrmTestLog.GridDblClick(Sender: TObject);
begin
 actTesting_CurrentTask.Execute;
end;

procedure TfrmTestLog.GridKeyPress(Sender: TObject; var Key: Char);
begin
 If Key = #13 then BeginTest(Grid.Row);
end;

procedure TfrmTestLog.SetResult(task_n, res_id:Integer);
begin
 with Grid do begin
  Cells[1, task_n] := Results[res_id];
  Update;
 end;
end;

procedure TfrmTestLog.InitHint(text:String);
var x0, y0:Integer;
begin
 hw := THintWindow.Create(Application);
(* x0 := fmWinOSA.Left + fmWinOSA.FileListBox1.Left +16;
 y0 := fmWinOSA.Top + fmWinOSA.FileListBox1.Top+16;
 hw.ActivateHint(Rect(x0,y0,
    x0+hw.Canvas.TextWidth(text)+16,
    y0+hw.Canvas.TextHeight(text)+4), text);        *)
end;

procedure TfrmTestLog.MoveHint;
var dx,dy:INteger;
    kx,ky:INteger;
    l:Double;
begin
 dx := destx-hw.Left;
 dy := desty-hw.Top;
 l := sqrt(sqr(dx)+sqr(dy));
 dy := Trunc(dy*16/l);
 dx := Trunc(dx*16/l);
 hw.Left := hw.Left + dx;
 hw.Top := hw.Top + dy;
end;

procedure TfrmTestLog.ShowHintAnim(dx,dy:Integer; fname:String);
var flag:Boolean;
begin
 destx := dx; desty := dy;
(* with fmWinOSA.FileListBox1 do begin
  Directory := ExtractFileDir(fname);
  ItemIndex := Items.IndexOf(ExtractFileName(fname));
 end;   *)

 InitHint(ExtractFileName(fname));
 Timer1.Enabled := true;
 while flag do begin
  Application.ProcessMessages;
  flag := Timer1.Enabled;
 end;
 hw.free;
end;

procedure TfrmTestLog.Timer1Timer(Sender: TObject);
begin
 MoveHint;
 timer1.Enabled := sqr(destx-hw.left)+sqr(desty-hw.Top)>256;
end;

procedure TfrmTestLog.actTesting_CurrentTaskExecute(Sender: TObject);
begin
 TestFlag := true;
 BeginTest(Grid.Row);
 TestFlag := false;
end;

procedure TfrmTestLog.miAskBeginClick(Sender: TObject);
begin
 TMenuItem(Sender).Checked :=  not TMenuItem(Sender).Checked;
end;

procedure TfrmTestLog.actTesting_AllTasksExecute(Sender: TObject);
var i:INteger;
    c1,c2,flag:Boolean;
begin
 TestFlag := true;
 AutoTest := true;
 TestStop := False;
 c1 := miAskBegin.Checked;
 c2 := miTestWait.Checked;
 miAskBegin.Checked := false;
 miTestWait.Checked := false;
 for i:=1 to TaskCount do begin
  Grid.Row := i;
  Application.ProcessMessages;
  BeginTest(i);
  Timer2.Enabled := true; flag := true;
  if i<TaskCount then Grid.Row := i+1;
  while flag do begin
   flag := Timer2.Enabled;
   Application.ProcessMessages;
  end;
  If TestStop Then Break;
 end;
 ShowMessage('������������ ��������.');
 miAskBegin.Checked := c1;
 miTestWait.Checked := c2;
 TestFlag := false;
 AutoTest := false;
 TestStop := False;
end;

procedure TfrmTestLog.Timer2Timer(Sender: TObject);
begin
 Timer2.Enabled := false;
end;

procedure TfrmTestLog.N5Click(Sender: TObject);
begin
TestStop:=true;
end;

Initialization
   WorkDir := ExtractFileDir(Application.ExeName);
   SampleDir := WorkDir + '\TestData\APK_ID_KRN\Sample';
   ResultDir := WorkDir + '\TestData\APK_ID_KRN\Result';
   EtalonDir := WorkDir + '\TestData\APK_ID_KRN\Result\EtResult';
end.
