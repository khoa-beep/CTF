# PATCH

Bài này mình nói về cách để patch một chương trình \( hay gọi tắt là crack chương trình or tìm ra key để bẻ khóa \)

{% file src="../../.gitbook/assets/patch.zip" caption="Patch" %}

Tải zip về và giải nén.

Ta chạy chương trình

![](../../.gitbook/assets/image%20%2819%29.png)

Có một thông điệp gì đó ở trong này mà bị che mất rồi.

Ta thử load vào IDA xem sao

./ Patch.exe: PE32+ executable \(GUI\) x86-64, for MS Windows

Chạy file này ta thấy được file này được code bằng giao dien GUI 32 or 64  bit trên windows

Mở IDA 64 Luôn nào.

Vì đây là chương trình này được tạo từ giao diện GUI tạo bằng WinAPI nên sẽ có hàm winmain

![](../../.gitbook/assets/image%20%2812%29.png)

Nhập theo hình

![](../../.gitbook/assets/image%20%2817%29.png)

IDA sẽ tìm đến hàm winmain

![](../../.gitbook/assets/image%20%2815%29.png)

Trỏ đến chuỗi đó và nhập x để tìm hàm gọi tham chiếu đến

Ta có được hàm winmain.

![](../../.gitbook/assets/image%20%2811%29.png)

Trong IDA có 1 chứ năng đọc mã lắp rắp mà theo tiêu chuẩn mình thì mã này chỉ đúng khoảng tầm 70 80 % thôi . Các ban cần có 1 chút kiến thức về hợp ngữ vững chắc thì dẽ rất dễ dàng.

Ta F5

```cpp
int __stdcall WinMain(HINSTANCE hInstance, HINSTANCE hPrevInstance, LPSTR lpCmdLine, int nShowCmd)
{
  HCURSOR v6; // rax
  HWND v7; // rax
  HWND v8; // rbx
  HACCEL v9; // rbx
  WNDCLASSEXW v11; // [rsp+60h] [rbp-A8h] BYREF
  struct tagMSG Msg; // [rsp+B0h] [rbp-58h] BYREF

  LoadStringW(hInstance, 0x67u, WindowName, 100);
  LoadStringW(hInstance, 0x6Du, ClassName, 100);
  v11.cbSize = 80;
  v11.style = 3;
  v11.lpfnWndProc = (WNDPROC)sub_1400032F0;
  *(_QWORD *)&v11.cbClsExtra = 0i64;
  v11.hInstance = hInstance;
  v11.hIcon = LoadIconW(hInstance, (LPCWSTR)0x6B);
  v6 = LoadCursorW(0i64, (LPCWSTR)0x7F00);
  *(__m128i *)&v11.hbrBackground = _mm_load_si128((const __m128i *)&xmmword_1400053F0);
  v11.hCursor = v6;
  v11.lpszClassName = ClassName;
  v11.hIconSm = LoadIconW(hInstance, (LPCWSTR)0x6C);
  RegisterClassExW(&v11);
  qword_140007880 = (__int64)&unk_1400078A0;
  v7 = CreateWindowExW(0, ClassName, WindowName, 0xC80000u, 0x80000000, 0, 600, 200, 0i64, 0i64, hInstance, 0i64);
  v8 = v7;
  if ( v7 )
  {
    hWnd = v7;
    dword_140007920 = 600;
    dword_140007924 = 200;
    GdiplusStartup(&unk_1400078A0, &dword_1400078A8, 0i64);
    ShowWindow(v8, nShowCmd);
    UpdateWindow(v8);
    v9 = LoadAcceleratorsW(hInstance, (LPCWSTR)0x6D);
    while ( GetMessageW(&Msg, 0i64, 0, 0) )
    {
      if ( !TranslateAcceleratorW(Msg.hwnd, v9, &Msg) )
      {
        TranslateMessage(&Msg);
        DispatchMessageW(&Msg);
      }
    }
    LODWORD(v7) = Msg.wParam;
  }
  return (int)v7;
}
```

Ta có thể thấy chức năng WinMain được dịch ngược bằng phím tắt F5 trong. Trong số đó, hàm RegisterClassExW là một hàm đăng ký một lớp cửa sổ và bạn có thể thấy rằng các biến v11 được nhập dưới dạng đối số. Phần quan trọng nhất ở đây là dòng 14, phần thiết lập gọi lại thông báo của cửa sổ.

Nói chung, hoạt động của cửa sổ được định nghĩa trong hàm gọi lại thông báo, vì vậy bạn cần phân tích hàm sub\_1400032F0 để biết nó thực hiện thao tác nào.

```cpp
LRESULT __fastcall sub_1400032F0(HWND a1, UINT a2, WPARAM a3, LPARAM a4)
{
  LRESULT result; // rax
  _QWORD *v5; // rbx
  __int64 v6; // rbx
  __int64 v7; // [rsp+20h] [rbp-18h] BYREF

  switch ( a2 )
  {
    case 2u:
      PostQuitMessage(0);
      result = 0i64;
      break;
    case 0xFu:
      qword_140007910 = (__int64)BeginPaint(hWnd, &Paint);
      v5 = (_QWORD *)GdipAlloc(16i64);
      if ( v5 )
      {
        *v5 = 0i64;
        v5[1] = 0i64;
        v7 = 0i64;
        *((_DWORD *)v5 + 2) = GdipCreateFromHDC(qword_140007910, &v7);
        *v5 = v7;
      }
      else
      {
        v5 = 0i64;
      }
      qword_140007918 = (__int64)v5;
      sub_140002C40();
      v6 = qword_140007918;
      if ( qword_140007918 )
      {
        GdipDeleteGraphics(*(_QWORD *)qword_140007918);
        GdipFree(v6);
      }
      EndPaint(hWnd, &Paint);
      result = 0i64;
      break;
    case 0x202u:
      InvalidateRect(hWnd, 0i64, 1);
      UpdateWindow(hWnd);
      result = 0i64;
      break;
    default:
      result = DefWindowProcW(a1, a2, a3, a4);
      break;
  }
  return result;
}
```

 Ta thấy được hàm beginpaint có nghĩa là bắt đầu vẽ một cái gì đó và hàm endpaint là kết thúc vẽ.

Ta để ý giữa 2 hàm đó có 1 hàm là 

```cpp
sub_140002C40();
```

Vô hàm này phân tích

```cpp
char __fastcall sub_140002C40(__int64 a1, int a2)
{
  int v2; // ebx
  int v3; // edx
  int v4; // edx
  int v5; // edx
  int v6; // edx
  int v7; // edx
  int v8; // edx
  int v9; // edx
  int v10; // edx
  int v11; // edx
  int v12; // edx
  int v13; // edx
  int v14; // edx
  int v15; // edx
  int v16; // edx
  int v17; // edx
  int v18; // edx
  int v19; // edx
  int v20; // edx
  int v21; // edx
  int v22; // edx
  int v23; // edx
  int v24; // edx
  int v25; // edx
  int v26; // edx
  __int64 v27; // rbx
  __int64 v28; // r8
  __int64 v29; // r8
  __int64 v30; // rdx
  __int64 v31; // r8
  __int64 v32; // rdx
  __int64 v33; // r8
  __int64 v34; // rdx
  __int64 v35; // r8
  __int64 v36; // rdx
  __int64 v37; // r8
  __int64 v38; // rdx
  __int64 v39; // r8
  __int64 v40; // rdx
  __int64 v41; // r8
  __int64 v42; // r8
  __int64 v43; // rdx
  __int64 v44; // r8
  __int64 v45; // r8
  __int64 v46; // rdx
  __int64 v47; // r8

  v2 = qword_140007880;
  nullsub_1(qword_140007880, a2, 30, 470, 80, -16777216);
  nullsub_1(v2, v3, 35, 470, 75, -16777216);
  nullsub_1(v2, v4, 40, 470, 70, -16777216);
  nullsub_1(v2, v5, 45, 470, 65, -16777216);
  nullsub_1(v2, v6, 50, 470, 60, -16777216);
  nullsub_1(v2, v7, 55, 470, 55, -16777216);
  nullsub_1(v2, v8, 60, 470, 50, -16777216);
  nullsub_1(v2, v9, 65, 470, 45, -16777216);
  nullsub_1(v2, v10, 70, 470, 40, -16777216);
  nullsub_1(v2, v11, 75, 470, 75, -16777216);
  nullsub_1(v2, v12, 80, 400, 60, -16777216);
  nullsub_1(v2, v13, 30, 470, 90, -16777216);
  nullsub_1(v2, v14, 35, 470, 30, -16777216);
  nullsub_1(v2, v15, 40, 470, 35, -16777216);
  nullsub_1(v2, v16, 45, 470, 50, -16777216);
  nullsub_1(v2, v17, 50, 470, 40, -16777216);
  nullsub_1(v2, v18, 55, 400, 90, -16777216);
  nullsub_1(v2, v19, 60, 470, 60, -16777216);
  nullsub_1(v2, v20, 65, 470, 30, -16777216);
  nullsub_1(v2, v21, 70, 470, 80, -16777216);
  nullsub_1(v2, v22, 75, 470, 70, -16777216);
  nullsub_1(v2, v23, 80, 470, 60, -16777216);
  nullsub_1(v2, v24, 80, 470, 80, -16777216);
  nullsub_1(v2, v25, 80, 470, 70, -16777216);
  nullsub_1(v2, v26, 90, 470, 90, -16777216);
  v27 = qword_140007880;
  sub_1400017A0(qword_140007880, 40i64, v28, 4278190080i64);
  sub_140001C80(v27, 80i64, v29, 4278190080i64);
  sub_140002640(v27, v30, v31, 4278190080i64);
  sub_1400020F0(v27, v32, v33, 4278190080i64);
  sub_140002390(v27, v34, v35, 4278190080i64);
  sub_140001240(v27, v36, v37, 4278190080i64);
  sub_140001F20(v27, v38, v39, 4278190080i64);
  sub_140001560(v27, v40, v41, 4278190080i64);
  sub_140001C80(v27, 360i64, v42, 4278190080i64);
  sub_1400019D0(v27, v43, v44, 4278190080i64);
  sub_1400017A0(v27, 440i64, v45, 4278190080i64);
  sub_140002870(v27, v46, v47, 4278190080i64);
  return 0;
}
```

Có nguyên 1 gì đó được gọi đi gọi lại như đệ quy thì phải ta nghĩ đây chắc hàm vẽ cái thông tin ta cần tìm nên ta sẽ patch chỗ này.

![](../../.gitbook/assets/image%20%2814%29.png)

![](../../.gitbook/assets/image%20%2820%29.png)

Kết quả sau khi pacth

![](../../.gitbook/assets/image%20%2818%29.png)

![](../../.gitbook/assets/image%20%2816%29.png)



Lưu lại ok và chạy thử

![](../../.gitbook/assets/image%20%2813%29.png)



TA đã thành công việc patch ct chạy.

