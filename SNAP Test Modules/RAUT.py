from framework.latentmodule import LatentModule
from direct.showbase import DirectObject

class Main(DirectObject.DirectObject, LatentModule):
    def __init__(self):
        LatentModule.__init__(self)

        # MARKERS LEGEND
        # 0: beginning
        # 10+: AUTs
        # 20+: RATs

        self.ratWait = 15                    # this will be the wait time for each trio in the RAT
        self.ratRounds = 25                  # number of word trios to be presented (number of elements in ratGroup)
        self.ratGroup1 = ["COTTAGE SWISS CAKE", "SHOW LIFE ROW", "DUCK FOLD DOLLAR", "ROCKING WHEEL HIGH", "FOUNTAIN BAKING SHOP",
                          "AID RUBBER WAGON", "CRACKER FLY FIGHTER", "CANE DADDY PLUM", "DREAM BREAK LIGHT", "POLITICAL SURPRISE LINE",
                          "PIECE MIND DATING", "FLOWER FRIEND SCOUT", "PRINT BERRY BIRD", "DATE ALLEY FOLD", "CADET CAPSULE SHIP",
                          "STICK MAKER POINT", "FOX MAN PEEP", "DUST CEREAL FISH", "FOOD FORWARD BREAK", "PEACH ARM TAR",
                          "PALM SHOE HOUSE", "WHEEL HAND SHOPPING", "HOME SEA BED", "SANDWICH HOUSE GOLF", "SAGE PAINT HAIR"]

        self.ratGroup2 = ["LOSER THROAT SPOT",  "NIGHT WRIST STOP", "DEW COMB BEE", "PRESERVE RANGER TROPICAL", "FLAKE MOBILE CONE",
                          "SAFETY CUSHION POINT", "FISH MINE RUSH", "MEASURE WORM VIDEO", "RIVER NOTE ACCOUNT", "HIGH DISTRICT HOUSE",
                          "WORM SHELF END", "SENSE COURTESY PLACE", "PIE LUCK BELLY", "OPERA HAND DISH", "FUR RACK TAIL",
                          "HOUND PRESSURE SHOT", "SLEEPING BEAN TRASH", "LIGHT BIRTHDAY STICK", "SHINE BEAM STRUCK", "WATER MINE SHAKER",
                          "BASKET EIGHT SNOW", "RIGHT CAT CARBON", "NUCLEAR FEUD ALBUM", "CROSS RAIN TIE", "FRENCH CAR SHOE"]

        self.autWait = 60                   # this will be the wait time for each object in the AUT
        self.autRounds = 1                  # number of objects to be presented (number of elements in autGroup)
        self.autGroup1a = ["BRICK"]
        self.autGroup1b = ["PAPERCLIP"]
        self.autGroup2a = ["BUTTON"]
        self.autGroup2b = ["NEWSPAPER"]



    #ENTER NUMBER OF DAY FOR PROPER TESTS
    def run(self):
        intro_string = self.write('Session 1: Press "1" \n Session 2: Press "2"',0)
        user_input = self.waitfor_multiple(['1','2'])

        if user_input[0] == '1':
            intro_string.destroy()
            self.test1()
        elif user_input[0] == '2':
            intro_string.destroy()
            self.test2()


    #DAY 1 TESTS
    def test1(self):
        self.sound('default_ding.wav', volume=0.5)
        self.marker('Pre')
        self.write('Please relax and wait for the headset to adjust.\nThe process should take about 2-minutes.', 10)
        self.sleep(110)

        # AUT1a
        self.sound('default_ding.wav', volume=0.5)
        self.marker('AUT1')
        self.write('In this test, you will be given a random object.\nYour task is to come up with as many novel uses for the object as you can.\nPress the space bar to continue.', 'space')
        self.write('These alternative uses should not be typical or virtually impossible.\nPress the space bar to continue.', 'space')
        self.write('Say your answers aloud as the audio of this session will be recorded.\nYou will be given %d seconds.\nPress the space bar to continue.' % self.autWait,'space')
        self.write('Notify us when you have completed the first portion.\nPress the space bar when you are ready to begin.', 'space')
        for i in range(self.autRounds):
            self.marker(10 + i)
            self.write(self.autGroup1a[i], self.autWait, scale=0.5)
            self.sleep(2)

        #WAIT FOR GAME TO BE FINISHED
        self.sound('default_ding.wav', volume=0.5)
        self.marker('GAME')
        self.write('You have completed the first portion.\nYou will now go through the experiment game.\nPress space bar once you have finished the game.', 'space')
        self.write('If you are finished with the game,\npress space bar to continue to the second portion of testing.', 'space')

        # RAT1
        self.sound('default_ding.wav', volume=0.5)
        self.marker('RAT')
        self.write('In this test, you will be shown a trio of words.\nYour task is to find the fourth word that the trio share.\nPress the space bar to continue.', 'space')
        self.write('For example, if you were shown CREAM SKATE CUBE...\nYou would want to answer with ICE.\nPress the space bar to continue.', 'space')
        self.write('Say your answers aloud as the audio of this session will be recorded.\nYou will be given %d seconds for each trio.\nIf you can not come up with the answer in time, move on.\nPress the space bar to continue.' % self.ratWait, 'space')
        self.write('If you figure out the answer early, wait until the next trio is shown.\nPress the space bar to continue.', 'space')
        self.write('Press the space bar when you are ready to begin.', 'space')
        for i in range(self.ratRounds):
            self.marker(20 + i)
            self.write(self.ratGroup1[i], self.ratWait, scale=0.2)
            self.sleep(2)

        # AUT1b
        self.sound('default_ding.wav', volume=0.5)
        self.marker('AUT2')
        self.write('In the next test, you will be told a random object.\nYour task is to come up with as many novel uses for the object as you can.\nPress the space bar to continue.', 'space')
        self.write('These alternative uses should not be typical or virtually impossible.\nPress the space bar to continue.', 'space')
        self.write('Say your answers aloud as the audio of this session will be recorded.\nYou will be given %d seconds.\nPress the space bar to begin.' % self.autWait, 'space')
        for i in range(self.autRounds):
            self.marker(10 + i)
            self.write(self.autGroup1b[i], self.autWait, scale=0.5)
            self.sleep(2)

        self.sound('default_ding.wav', volume=0.5)
        self.marker('Post')
        self.write('Please relax while the headset finishes collecting data.\nThe process should take about 2-minutes.', 10)
        self.sleep(110)

        self.sound('default_ding.wav', volume=0.5)
        self.write('Please notify us that you have finished the experiment. Thank you.', 10)

    # DAY 2 TESTS
    def test2(self):
        self.sound('default_ding.wav', volume=0.5)
        self.marker('Pre')
        self.write('Please relax and wait for the headset to adjust.\nThe process should take about 2-minutes.', 10)
        self.sleep(110)

        # AUT2a
        self.sound('default_ding.wav', volume=0.5)
        self.marker('AUT1')
        self.write('In this test, you will be given a random object.\nYour task is to come up with as many novel uses for the object as you can.\nPress the space bar to continue.', 'space')
        self.write('These alternative uses should not be typical or virtually impossible.\nPress the space bar to continue.', 'space')
        self.write('Say your answers aloud as the audio of this session will be recorded.\nYou will be given %d seconds.\nPress the space bar to continue.' % self.autWait,'space')
        self.write('Notify us when you have completed the first portion.\nPress the space bar when you are ready to begin.', 'space')
        for i in range(self.autRounds):
            self.marker(10 + i)
            self.write(self.autGroup2a[i], self.autWait, scale=0.5)
            self.sleep(2)

        #WAIT FOR GAME TO BE FINISHED
        self.sound('default_ding.wav', volume=0.5)
        self.marker('GAME')
        self.write('You have completed the first portion.\nYou will now go through the experiment game.\nPress space bar once you have finished the game.', 'space')
        self.write('If you are finished with the game,\npress space bar to continue to the second portion of testing.', 'space')

        # RAT2
        self.sound('default_ding.wav', volume=0.5)
        self.marker('RAT')
        self.write('In this test, you will be shown a trio of words.\nYour task is to find the fourth word that the trio share.\nPress the space bar to continue.', 'space')
        self.write('For example, if you were shown CREAM SKATE CUBE...\nYou would want to answer with ICE.', 'space')
        self.write('Say your answers aloud as the audio of this session will be recorded.\nYou will be given %d seconds for each trio.\nIf you can not come up with the answer in time, move on.\nPress the space bar to continue.' % self.ratWait, 'space')
        self.write('If you figure out the answer early, wait until the next trio is shown.\nPress the space bar to continue.', 'space')
        self.write('Press the space bar when you are ready to begin.', 'space')
        for i in range(self.ratRounds):
            self.marker(20 + i)
            self.write(self.ratGroup2[i], self.ratWait, scale=0.2)
            self.sleep(2)

        # AUT2b
        self.sound('default_ding.wav', volume=0.5)
        self.marker('AUT2')
        self.write('In the next test, you will be told a random object.\nYour task is to come up with as many novel uses for the object as you can.\nPress the space bar to continue.', 'space')
        self.write('These alternative uses should not be typical or virtually impossible.\nPress the space bar to continue.', 'space')
        self.write('Say your answers aloud as the audio of this session will be recorded.\nYou will be given %d seconds.\nPress the space bar to begin.' % self.autWait, 'space')
        for i in range(self.autRounds):
            self.marker(10 + i)
            self.write(self.autGroup2b[i], self.autWait, scale=0.5)
            self.sleep(2)

        self.sound('default_ding.wav', volume=0.5)
        self.marker('Post')
        self.write('Please relax while the headset finishes collecting data.\nThe process should take about 2-minutes.', 10)
        self.sleep(110)

        self.sound('default_ding.wav', volume=0.5)
        self.write('Please notify us that you have finished the experiment. Thank you.', 10)
