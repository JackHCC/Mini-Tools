import sys
import os
from os.path import expanduser
from PyQt5.QtWidgets import *
from PyQt5.QtMultimedia import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUiType
import time

scriptDir = os.path.dirname(os.path.realpath(__file__))
SCREEN,_ = loadUiType(os.path.join(os.path.dirname(__file__),"first.ui"))
PLAYER,_ = loadUiType(os.path.join(os.path.dirname(__file__),"player.ui"))

class Threading(QThread):
    mysignal = pyqtSignal(int)
    def __init__(self, parent=None):
        QThread.__init__(self, parent)

    def run(self):
        time.sleep(4)
        self.mysignal.emit(1)

class ThreadAnimation(QThread):
    myAnimation = pyqtSignal(int)
    def __init__(self, parent=None):
        QThread.__init__(self, parent)
        self.runs = True
    def run(self):
        while self.runs:
            time.sleep(2)
            self.myAnimation.emit(1)
    def stop(self):
        self.runs = False
        
class Screen(QMainWindow, SCREEN):
    def __init__(self, parent=None):
        super(Screen, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setWindowIcon(QIcon(scriptDir + os.path.sep + 'icons/heart.ico'))
        self.setupUi(self)
        pitmap = QPixmap("icons/heart.ico")
        self.image.setPixmap(pitmap)
        thread = Threading(self)
        thread.mysignal.connect(self.onTimeEnd)
        thread.start()
        
    @pyqtSlot(int)
    def onTimeEnd(self, value):
        self.hide()
        window = Player(self)
        window.show()

        
class Player(QMainWindow, PLAYER):
    def __init__(self, parent=None):
        super(Player, self).__init__(parent)
        self.setupUi(self)
        self.setWindowIcon(QIcon(scriptDir + os.path.sep + 'icons/heart.ico'))
        self.play_icon = QIcon("icons/play.png")
        self.next_icon = QIcon("icons/next.png")
        self.back_icon = QIcon("icons/back.png")
        self.pause_icon = QIcon("icons/pause.png")
        self.stop_icon = QIcon("icons/stop.png")
        self.volume_icon = QIcon("icons/volume.png")
        self.mute_icon = QIcon("icons/mute.png")
        self.default_image = QPixmap("icons/heart.ico")
        self.currentPlaylist = QMediaPlaylist()
        self.icon_button()
        self.setAcceptDrops(True)
        self.sound = True
        self.music = {}
        self.player = QMediaPlayer(self)
        self.player.mediaStatusChanged.connect(self.mediaStatusChange)
        self.player.positionChanged.connect(self.positionChanged)
        self.player.durationChanged.connect(self.durationChanged)
        self.musicList.itemClicked.connect(self.on_item_clicked)
        self._buffer = QBuffer()
        self.musicProgress.setValue(0)
        self.musicProgress.setRange(0, 0)
        self.musicProgress.sliderMoved.connect(self.onSliderMoved)
        self.musicVolume.valueChanged.connect(self.onVolumeChange)
        self.player.setPlaylist(self.currentPlaylist)
        self.volumeProgress.clicked.connect(self.onSoundClicked)
        self.stopButton.clicked.connect(self.onStopClicked)
        self.nextButton.clicked.connect(self.onNextClicked)
        self.backButton.clicked.connect(self.onBackClicked)
        self.playButton.clicked.connect(self.onPlayClicked)
        self.pauseButton.clicked.connect(self.onPauseClicked)
        self.musicVolume.setValue(50)
        self.index = 0
        self.item = ""
        self.animation = ThreadAnimation(self)
        self.animation.myAnimation.connect(self.startAni)
        self.animation.start()
        self.aniType = "left"
        
    def onVolumeChange(self, value):
        self.player.setVolume(value)
    def onNextClicked(self):
        self.player.playlist().next()
        index = self.player.playlist().currentIndex()
        try:
            self.musicList.item(index).setSelected(True)
        except:
            self.player.playlist().setCurrentIndex(0)
            self.musicList.item(0).setSelected(True)
            self.player.play()
    def onBackClicked(self):
        self.player.playlist().previous()
        index = self.player.playlist().currentIndex()
        try:
            self.musicList.item(index).setSelected(True)
        except:
            self.player.playlist().setCurrentIndex(0)
            self.musicList.item(0).setSelected(True)
            self.player.play()
            
    def onPlayClicked(self):
        if self.currentPlaylist.mediaCount() == 0:
            self.openFile()
            return
        if self.player.state() == QMediaPlayer.PausedState:
            self.player.play()
        elif self.player.state() == QMediaPlayer.StoppedState:
            self.player.play()
        elif self.player.state() == QMediaPlayer.PlayingState:
            return
        else:
            self.player.play()
            
    def openFile(self):
        fileChoosen = QFileDialog.getOpenFileUrl(self, 'Open Music File', expanduser('~'),'Audio (*.mp3 *.ogg *.wav)','*.mp3 *.ogg *.wav')
        if fileChoosen != None:
            self.musicList.addItem(fileChoosen[0].fileName())
            self.currentPlaylist.addMedia(QMediaContent(fileChoosen[0]))
            
    def onPauseClicked(self):
        if self.player.state() == QMediaPlayer.PausedState:
            self.player.play()
        elif self.player.state() == QMediaPlayer.StoppedState:
            self.player.play()
        else:
            self.player.pause()
    
    def onStopClicked(self):
        if self.player.state() == QMediaPlayer.PlayingState:
            self.player.stop()
        elif self.player.state() == QMediaPlayer.PausedState:
            self.player.stop()
        
    def onSoundClicked(self):
        if self.sound:
            self.volumeProgress.setIcon(self.mute_icon)
            self.player.setVolume(0)
            self.sound = False
        else:
            self.sound = True
            self.player.setVolume(self.musicVolume.value())
            self.volumeProgress.setIcon(self.volume_icon)
        
    def durationChanged(self, duration):
        self.musicProgress.setRange(0, duration)
        
    def onSliderMoved(self, position):
        sender = self.sender()
        if isinstance(sender, QSlider):
            if self.player.isSeekable():
                self.player.setPosition(position)
                
    def on_item_clicked(self, item):
        data = self.musicList.selectedIndexes()[0]
        index = data.row()
        self.playMusic(index=index)
        
    def playMusic(self, index=0):
        self.player.setPlaylist(self.currentPlaylist)
        self.player.playlist().setCurrentIndex(index)
        self.player.play()
        self.player.setVolume(self.musicVolume.value())
        
    
    def onVolumeChange(self, value):
        if value > 50:
            self.player.setVolume(value+1)
        else:
            self.player.setVolume(value)
        
    def positionChanged(self, position):
        tm = '%d:%02d'%(int(position/60000),int((position/1000)%60))
        self.startTime.setText(tm)
        self.musicProgress.setValue(position)
                
    def mediaStatusChange(self):
        durationT = self.player.duration()
        tm = "%d:%02d"%(int(durationT/60000),int((durationT/1000)%60))
        self.musicTime.setText(tm)
        index = self.player.playlist().currentIndex()
        try:
            self.musicList.item(index).setSelected(True)
        except:
            pass
        
    def icon_button(self):
        self.playButton.setIcon(self.play_icon)
        self.pauseButton.setIcon(self.pause_icon)
        self.nextButton.setIcon(self.next_icon)
        self.backButton.setIcon(self.back_icon)
        self.stopButton.setIcon(self.stop_icon)
        self.image.setPixmap(self.default_image)
        self.image.setAlignment(Qt.AlignCenter)
        self.volumeProgress.setIcon(self.volume_icon)


    def dropEvent(self, e):
        for x in e.mimeData().urls():
            mp3 = x.toString()
            name = x.fileName()
            path = x.toLocalFile()
            self.musicList.addItem(name)
            self.currentPlaylist.addMedia(QMediaContent(QUrl.fromLocalFile(path)))
            
    def dragEnterEvent(self, e):
        for x in e.mimeData().urls():
            mp3 = x.toString()
            if mp3.endswith(".mp3") or mp3.endswith(".MP3"):
                e.accept()
            else:
                e.ignore()
                
    def closeEvent(self, event):
        reply = QMessageBox.question(self,'Exit?','Are you sure you want to close?',QMessageBox.Yes|QMessageBox.No,QMessageBox.Yes)
        if reply == QMessageBox.Yes :
            qApp.quit()
        else :
            try:
                event.ignore()
            except AttributeError:
                pass
            
    @pyqtSlot(int)
    def startAni(self, i):
        anim = QPropertyAnimation(self.image, b"geometry")
        anim.setDuration(30)
        if self.aniType == "left":
            anim.setStartValue(QRect(180, 100, 411, 271))
            anim.setEndValue(QRect(190, 110, 420, 280))
            self.aniType = "right"
        elif self.aniType == "right":
            anim.setStartValue(QRect(190, 110, 420, 280))
            anim.setEndValue(QRect(180, 100, 411, 271))
            self.aniType = "dort"
        elif self.aniType == "dort":
            anim.setStartValue(QRect(180, 100, 411, 271))
            anim.setEndValue(QRect(122, 302, 395, 261))
            self.aniType = "left"
        anim.start()

if __name__ == "__main__":
    app=QApplication(sys.argv)
    window = Screen()
    window.show()
    app.exec_()
