# youtube 음원 추출 예제 소스코드



## 준비물

### 1. choco

윈도우 환경에서 필요한 패키지들을 설치하기 위해 choco를 설치한다.

```sh
# 관리자 창으로 powershell을 열은 뒤 복사 붙여넣기

Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))
```

choco설치 참고 https://blog.itpaper.co.kr/win-choco/



### 2.  ffmpeg

```powershell
choco install ffmpeg
```



### 3. python

python 설치 참고 https://wikidocs.net/8

(최신버전을 설치하면 된다.)

```sh
python --version # 파이썬 버전확인
pip --version	 # pip 버전확인
```

> pip는 python 설치시 자동으로 설치된다



### 4. youtube_dl

python의 youtube_dl라이브러리를 이용하여 음원을 추출할 것 이기 떄문에 해당 라이브러리를 설치한다.

```powershell
pip install youtube_dl
```

youtube_dl 예제코드 https://www.programcreek.com/python/example/98358/youtube_dl.YoutubeDL

## 사용 방법

clone받은 run.py파일을 실행시켜주면 된다.

```sh
# 현재 디렉토리에서
python run.py
```

실행 시 다음과 같이 콘솔에 다음과 같이 뜨게 되는데

![실행화면](https://github.com/shoon2430/keep-my-music/blob/master/img/실행화면.png)

커서에 추출 하고 싶은 동영상의 주소를 넣어주면 된다.

![결과](https://github.com/shoon2430/keep-my-music/blob/master/img/결과.png)

주소를 넣어 준 뒤 Enter를 누르게 되면 내가 지정한 위치에 mp3파일이 저장된것을 확인 할 수 있다.

![파일저장결과](https://github.com/shoon2430/keep-my-music/blob/master/img/파일저장결과.png)

