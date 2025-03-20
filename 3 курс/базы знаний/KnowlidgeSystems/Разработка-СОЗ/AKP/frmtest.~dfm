object frmTestLog: TfrmTestLog
  Left = 201
  Top = 193
  Width = 456
  Height = 236
  Caption = #1055#1088#1086#1090#1086#1082#1086#1083' '#1090#1077#1089#1090#1080#1088#1086#1074#1072#1085#1080#1103
  Color = clBtnFace
  Font.Charset = DEFAULT_CHARSET
  Font.Color = clWindowText
  Font.Height = -11
  Font.Name = 'MS Sans Serif'
  Font.Style = []
  Menu = MainMenu1
  OldCreateOrder = False
  OnCreate = FormCreate
  OnResize = FormResize
  PixelsPerInch = 96
  TextHeight = 13
  object Grid: TStringGrid
    Left = 0
    Top = 41
    Width = 440
    Height = 136
    Align = alClient
    DefaultRowHeight = 20
    Options = [goFixedVertLine, goFixedHorzLine, goVertLine, goHorzLine]
    TabOrder = 0
    OnDblClick = GridDblClick
    OnDrawCell = GridDrawCell
    OnKeyPress = GridKeyPress
    OnSelectCell = GridSelectCell
  end
  object Panel1: TPanel
    Left = 0
    Top = 0
    Width = 440
    Height = 41
    Align = alTop
    TabOrder = 1
    Visible = False
    object btnClose: TButton
      Left = 272
      Top = 8
      Width = 129
      Height = 25
      Caption = #1047#1072#1082#1088#1099#1090#1100
      TabOrder = 0
      OnClick = btnCloseClick
    end
  end
  object Timer1: TTimer
    Enabled = False
    Interval = 1
    OnTimer = Timer1Timer
    Left = 32
    Top = 88
  end
  object MainMenu1: TMainMenu
    Left = 136
    Top = 8
    object N1: TMenuItem
      Caption = #1058#1077#1089#1090#1080#1088#1086#1074#1072#1085#1080#1077
      object N2: TMenuItem
        Action = actTesting_CurrentTask
      end
      object N3: TMenuItem
        Action = actTesting_AllTasks
      end
    end
    object N4: TMenuItem
      Caption = #1054#1087#1094#1080#1080
      object miAskBegin: TMenuItem
        Caption = #1047#1072#1087#1088#1072#1096#1080#1074#1072#1090#1100' '#1085#1072#1095#1072#1083#1086' '#1090#1077#1089#1090#1080#1088#1086#1074#1072#1085#1080#1103
        Checked = True
        OnClick = miAskBeginClick
      end
      object miTestWait: TMenuItem
        Caption = #1054#1089#1090#1072#1085#1086#1074#1082#1072' '#1074#1086' '#1074#1088#1077#1084#1103' '#1090#1077#1089#1090#1080#1088#1074#1072#1085#1080#1103
        Checked = True
        OnClick = miAskBeginClick
      end
      object N5: TMenuItem
        Caption = #1054#1089#1090#1072#1085#1086#1074#1082#1072' '#1090#1077#1089#1090#1080#1088#1086#1074#1072#1085#1080#1103
        OnClick = N5Click
      end
    end
  end
  object ActionList1: TActionList
    Left = 88
    Top = 8
    object actTesting_CurrentTask: TAction
      Caption = #1042#1099#1073#1088#1072#1085#1085#1086#1081' '#1079#1072#1076#1072#1095#1080
      OnExecute = actTesting_CurrentTaskExecute
    end
    object actTesting_AllTasks: TAction
      Caption = #1042#1089#1077' '#1079#1072#1076#1072#1095#1080
      OnExecute = actTesting_AllTasksExecute
    end
  end
  object Timer2: TTimer
    Enabled = False
    Interval = 2000
    OnTimer = Timer2Timer
    Left = 48
    Top = 8
  end
end
