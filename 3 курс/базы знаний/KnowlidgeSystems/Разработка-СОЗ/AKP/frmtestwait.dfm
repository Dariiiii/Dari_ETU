object frmWait: TfrmWait
  Left = 176
  Top = 172
  BorderStyle = bsDialog
  Caption = #1057#1086#1086#1073#1097#1077#1085#1080#1077
  ClientHeight = 189
  ClientWidth = 416
  Color = clBtnFace
  Font.Charset = DEFAULT_CHARSET
  Font.Color = clWindowText
  Font.Height = -11
  Font.Name = 'MS Sans Serif'
  Font.Style = []
  FormStyle = fsStayOnTop
  OldCreateOrder = False
  OnShow = FormShow
  PixelsPerInch = 96
  TextHeight = 13
  object Label1: TLabel
    Left = 8
    Top = 8
    Width = 401
    Height = 137
    AutoSize = False
    Caption = 'Label1'
    WordWrap = True
  end
  object Panel1: TPanel
    Left = 0
    Top = 144
    Width = 409
    Height = 41
    BevelOuter = bvNone
    TabOrder = 0
    object btnOK: TButton
      Left = 168
      Top = 16
      Width = 89
      Height = 25
      Caption = 'OK'
      TabOrder = 0
      OnClick = btnOKClick
    end
  end
  object Panel2: TPanel
    Left = -8
    Top = 148
    Width = 417
    Height = 41
    BevelOuter = bvNone
    TabOrder = 1
    object btnYes: TButton
      Left = 136
      Top = 8
      Width = 75
      Height = 25
      Caption = #1044#1072
      TabOrder = 0
      OnClick = btnYesClick
    end
    object MR_NO: TButton
      Left = 232
      Top = 8
      Width = 75
      Height = 25
      Caption = #1053#1077#1090
      TabOrder = 1
      OnClick = MR_NOClick
    end
  end
end
