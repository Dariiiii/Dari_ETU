unit Tipe;

interface

const
 nword=40;

type
  String40 = String[NWord];
  tips = (integ,rel, wrd);
  domen = record case kind:tips of integ:(di:integer);
            rel:(dr:real); wrd:(dw:string40);end;
(*var
FlagPrObl:Boolean;{������� ������� ���������� �������}
Auto:Boolean;{������� ������ ������}
Fuzzi:Boolean;{������� ������������� ������������� �������}
ExeName:String;
Exe_Flag:Boolean;
ValueExe:String40;
Flag13:Boolean;  *)

implementation

end.
