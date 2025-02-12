import wx
import wikipedia
import wolframalpha
import pyttsx3

class OlusFrame(wx.Frame):
    
    # Initialize pyttsx3 engine for text-to-speech
    def __init__(self):
        wx.Frame.__init__(self, 
                          None, 
                          pos=wx.DefaultPosition,
                          size=wx.Size(450, 100),
                          style=wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX | wx.CLIP_CHILDREN,
                          title="Gabby Sam David")
        
        self.speaker = pyttsx3.init()  # Initialize pyttsx3 engine
        self.speaker.setProperty('rate', 150)  # Set the speech speed (words per minute)
        self.speaker.setProperty('volume', 1)  # Set the volume (0.0 to 1.0)

        panel = wx.Panel(self)
        my_sizer = wx.BoxSizer(wx.VERTICAL)
        lbl = wx.StaticText(panel, label="Hello Gabby Sam David! I am your digital assistant! How can I help you today?")
        
        my_sizer.Add(lbl, 0, wx.ALL, 5)
        self.txt = wx.TextCtrl(panel, style=wx.TE_PROCESS_ENTER, size=(400,30))
        self.txt.SetFocus()
        self.txt.Bind(wx.EVT_TEXT_ENTER, self.OnEnter)
        my_sizer.Add(self.txt, 0, wx.ALL, 5)
        panel.SetSizer(my_sizer)
        self.Show()

    def OnEnter(self, event):
        userinput = self.txt.GetValue()
        userinput = userinput.lower()

        if "who is " in userinput:
            userinput = userinput.strip("who is ")

        # Exit the application
        if userinput == 'exit':
            self.speaker.say("Goodbye!")
            self.speaker.runAndWait()
            exit()

        try:  # Try WolframAlpha API for answers
            app_id = "9GPURP-JKR4XYVQ8W"  # Your WolframAlpha API key
            client = wolframalpha.Client(app_id)
            result = client.query(userinput)
            answer = next(result.results).text

            print(answer)  # Print the answer
            self.speaker.say(answer)  # Speak the answer
            self.speaker.runAndWait()

        except:  # Fallback to Wikipedia search if WolframAlpha fails
            print("Sorry, I could not find an answer on WolframAlpha. Searching Wikipedia...")
            self.speaker.say("Sorry, I could not find an answer on WolframAlpha. Searching Wikipedia.")  # Let the user know
            self.speaker.runAndWait()

            userinput = userinput.split(" ")

            stopwords = ["and", "or", "never", "not", "what", "why", "how", "many", "are", "the", "a", "was", "were", "did", "which", "will", "be", "would", "could", "should", "can", "shall", "is"]

            # Remove stop words from the input
            userinput = [i for i in userinput if i not in stopwords]
            userinput = " ".join(userinput)

            try:
                # Searching Wikipedia (if WolframAlpha didn't return an answer)
                summary = wikipedia.summary(userinput, sentences=2)
                print(summary)
                self.speaker.say(summary)  # Speak the Wikipedia summary
                self.speaker.runAndWait()

            except wikipedia.exceptions.DisambiguationError as e:
                self.speaker.say("Sorry, there are multiple results. Please clarify your query.")  # Speak if there's ambiguity
                self.speaker.runAndWait()
            except wikipedia.exceptions.HTTPError:
                self.speaker.say("Sorry, I couldn't access Wikipedia. Please check your connection.")  # Handle HTTP errors
                self.speaker.runAndWait()

if __name__ == "__main__":
    app = wx.App(True)
    frame = OlusFrame()
    app.MainLoop()
