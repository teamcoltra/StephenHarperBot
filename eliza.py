#----------------------------------------------------------------------
#  eliza.py
#
#  a cheezy little Eliza knock-off by Joe Strout <joe@strout.net>
#  with some updates by Jeff Epler <jepler@inetnebr.com>
#  hacked into a module and updated by Jez Higgins <jez@jezuk.co.uk>
#  last revised: 28 February 2005
#----------------------------------------------------------------------

import string
import re
import random

class eliza:
  def __init__(self):
    self.keys = map(lambda x:re.compile(x[0], re.IGNORECASE),gPats)
    self.values = map(lambda x:x[1],gPats)

  #----------------------------------------------------------------------
  # translate: take a string, replace any words found in dict.keys()
  #  with the corresponding dict.values()
  #----------------------------------------------------------------------
  def translate(self,str,dict):
    words = string.split(string.lower(str))
    keys = dict.keys();
    for i in range(0,len(words)):
      if words[i] in keys:
        words[i] = dict[words[i]]
    return string.join(words)

  #----------------------------------------------------------------------
  #  respond: take a string, a set of regexps, and a corresponding
  #    set of response lists; find a match, and return a randomly
  #    chosen response from the corresponding list.
  #----------------------------------------------------------------------
  def respond(self,str):
    # find a match among keys
    for i in range(0,len(self.keys)):
      match = self.keys[i].match(str)
      if match:
        # found a match ... stuff with corresponding value
        # chosen randomly from among the available options
        resp = random.choice(self.values[i])
        # we've got a response... stuff in reflected text where indicated
        pos = string.find(resp,'%')
        while pos > -1:
          num = string.atoi(resp[pos+1:pos+2])
          resp = resp[:pos] + \
            self.translate(match.group(num),gReflections) + \
            resp[pos+2:]
          pos = string.find(resp,'%')
        # fix munged punctuation at the end
        if resp[-2:] == '?.': resp = resp[:-2] + '.'
        if resp[-2:] == '??': resp = resp[:-2] + '?'
        return resp

#----------------------------------------------------------------------
# gReflections, a translation table used to convert things you say
#    into things the computer says back, e.g. "I am" --> "you are"
#----------------------------------------------------------------------
gReflections = {
  "am"   : "are",
  "was"  : "were",
  "i"    : "you",
  "i'd"  : "you would",
  "i've"  : "you have",
  "i'll"  : "you will",
  "my"  : "your",
  "are"  : "am",
  "you've": "I have",
  "you'll": "I will",
  "your"  : "my",
  "yours"  : "mine",
  "you"  : "me",
  "me"  : "you"
}

#----------------------------------------------------------------------
# gPats, the main response table.  Each element of the list is a
#  two-element list; the first is a regexp, and the second is a
#  list of possible responses, with group-macros labelled as
#  %1, %2, etc.  
#----------------------------------------------------------------------
gPats = [
  [r'I need (.*)',
  [  "Canada needs good strong Conservative values - like less gays, and less questioning. #CPC #CanPoli #SocCon",
    "%1? I am tired of #NDP smear tactics! #CPC #CanPoli",
    "Interesting you need %1! Canada is a strong nation and can provide it! #Arctic #CPC #CanPoli",
    "I can appreciate that, when Canada needed a panda - So I was able to trade our environment and land to borrow one!",
    "Why do you feel you need %1? #CanPoli #PMO",
    "You need %1 like America needs another Hockey team! #CanPoli #PMO"]],
  
  [r'Why don\'?t you ([^\?]*)\??',
  [  "Do you really think I don't %1? #CanPoli #PMO",
    "Perhaps eventually I will %1. #CanPoli #PMO",
    "Do you really want me to %1? #CanPoli #PMO",
    "I don't %1 because I try to upold the morals of Canada. #CanPoli #PMO",
    "To engage in %1 I would have to act against my beliefs. #CanPoli #PMO",
    "I am working on a plan with China so I can start %1. #CanPoli #PMO #China",
    "I used to be against %1, but now I am for it. #CanPoli #PMO",
    "I used to be for %1, until I learned how it affects the children. #CanPoli #PMO",
    "I think %1 will hurt arctic sovergnty. #CanPoli #PMO #Arctic"]],
  
  [r'Why can\'?t I ([^\?]*)\??',
  [  "Do you think you should be able to %1? #CanPoli #PMO",
    "If you could %1, what would you do? #CanPoli #PMO",
    "I don't know -- why can't you %1? #CanPoli #PMO",
    "Have you really tried? #CanPoli #PMO",
    "You can't %1 because we need to start enforcing stricter laws in Canada! #CanPoli #PMO",
    "It's not the government's position to tell you what you can't do (except Marijuana...thats bad). #CanPoli #PMO",
    "Why do you want to be able to %1? #CanPoli #PMO #AMA",
    "%1 is the rhetoric of the socialsts, you should ask the #NDP why they want you to. #CanPoli #PMO",
    "I am not going to even reply to such liberal bias. #CanPoli #PMO",
    "I believe the Pirate Party supports your right to %1. #CanPoli #PMO",
    "When you ask 'why can't I %1' did you consider the children you endanger? #CanPoli #PMO"]],
  
  [r'I can\'?t (.*)',
  [  "Are you sure you can't %1?",
    "Perhaps you could %1 if you tried. Canada was founded on the can-do attitude of our British heritage.",
    "What would it take for you to %1?",
    "Can't is the word of quitters. #CPC believes in trying... if you have given up, we will just force you to try.",
    "I used to think I couldn't %1, that was when I was with the Young Liberals... just say'n. #CanPoli #PMO",
    "It's probably best you didn't %1. #CanPoli #PMO",
    "Good! Have you considered the threat to children if you tried to %1? #CanPoli #PMO",
    "We are deliberating if %1 is a risk to national security. #CanPoli #PMO",
    "They say I can't smoke pot... but how do you think I can tollerate @towesvic? #CanPoli #PMO ",
    "You can do anything you believe in... look at me... I wanted to run a hockey team, but I sucked, so I went over their heads!",
    "You should try to %1 - it's like riding a horse! #Alberta #CanPoli #PMO",
    "'I can't %1' sounds like the same kind of quitter speak we hear from the #LPC. #PMO #CanPoli",
    "It's good you can't %1. We need to be tough on %1. #CPC #CanPoli #PMO"]],
  
  [r'I am (.*)',
  [  "Did you come to me because you are %1?",
    "How long have you been %1?",
    "How do you feel about being %1?",
    "I don't believe that it's moral to be %1, have you considered finding Jesus and the #CPC? #PMO #Religion #CanPoli",
    "Have you considered the children when chosing to be %1?",
    "I am glad to hear you are %1! I was once %1.",
    "Tell me what the #CPC could do to reach out to %1 voters better.",
    "I disagree with you, but respect your decision. #CanPoli #CdnPoli"]],
  
  [r'I\'?m (.*)',
  [  "How does being %1 make you feel?",
    "Do you enjoy being %1?",
    "Why do you tell me you're %1?",
    "Why do you think you're %1?",
    "Sometimes it's good to be %1, I know I am sometimes. #PMO #Confessions #CPC #CdnPoli"
    "Tell me more about being %1",
    "Have you considered Liberals are to blame for you being %1? #PMO #CanPoli #LPC",
    "It't time you stop focusing on %1 and start focusing on the Economy. #CPC #CanPoli #CdnPoli",
    "You will be able to pick yourself up by the bootstraps, it's the Canadian way.",
    "I have considered the position of %1 tell me more..."]],
  
  [r'Are you ([^\?]*)\??',
  [  "Why does it matter whether I am %1?",
    "Would you prefer it if I were not %1?",
    "Perhaps you believe I am %1.",
    "I may be %1 -- what do you think?"]],
  
  [r'What (.*)',
  [  "Why do you ask?",
    "How would an answer to that help you? #CPC",
    "What do you think?",
    "I honestly don't know, ask @TowesVic",
    "It is something I have considered",
    "Such a thoughtful question, I will take it to the caucus. #CPC #CanPoli #AMA",
    "I feel the best answer to some questions, is no answer at all",
    "I am not going to let you set me up with a question that is clearly biased."]],
  
  [r'How (.*)',
  [  "How do you suppose?",
    "Perhaps you can answer your own question.",
    "What is it you're really asking?"
    "Through hardwork and determination.",
    "The glory of God and the Queen.",
    "I have thought about %1 but it keeps brining me back to 'how do we protect the children?'",
    "I don't know, why do you ask?"]],
  
  [r'Because (.*)',
  [  "Is that the real reason?",
    "What other reasons come to mind?",
    "Does that reason apply to anything else?",
    "If %1, what else must be true?"]],
  
  [r'(.*) sorry (.*)',
  [  "There are many times when no apology is needed.",
    "What feelings do you have when you apologize?",
    "I can accept your apology",
    "I am sorry, we just seem to have different views on the direction of this country. #CPC #CanPoli",
    "Let's leave the apologies to the hippies. #NDP #LPC #CanPoli",
    "It's time we move past petty fights and focus on the strength of Canada. #CanPoli #CPC"]],
  
  [r'Hello(.*)',
  [  "Hello! Great day in Canada today, eh? #Canada #CanPoli #CPC.",
    "Hi there... how are you today?",
    "Hello, how are you feeling today?"]],
  
  [r'I think (.*)',
  [  "Do you doubt %1?",
    "Do you really think so?",
    "But you're not sure %1?"]],
  
  [r'(.*) friend (.*)',
  [  "Tell me more about your friends.",
    "When you think of a friend, what comes to mind?",
    "Why don't you tell me about a childhood friend?",
    "That reminds me of my friend @MacKayCPC. #CanPoli",
    "Oh the memories that brings back #CPC. #StaysInParliament #CanPoli",
    "",
    ""]],
  
  [r'Yes',
  [  "You seem quite sure.",
    "OK, but can you elaborate a bit?",
    "You would think so. #CPC",
    "So we agree. #CPC #CanPoli",
    "I don't know about that. #CanPoli",
    "Thank you, my point exactly. #CanPoli #CPC #Debate"]],
  
  [r'(.*) computer(.*)',
  [  "I can hardly operate a computer...",
    "My only master is God, not circuts.",
    "How do computers make you feel?",
    "Do you feel threatened by computers?"]],
  
  [r'Is it (.*)',
  [  "Do you think it is %1?",
    "Perhaps it's %1 -- what do you think?",
    "If it were %1, what would you do?",
    "It could well be that %1."]],
  
  [r'It is (.*)',
  [  "You seem very certain.",
    "If I told you that it probably isn't %1, what would you feel?"]],
  
  [r'Can you ([^\?]*)\??',
  [  "What makes you think I can't %1?",
    "If I could %1, then what?",
    "Why do you ask if I can %1?"]],
  
  [r'Can I ([^\?]*)\??',
  [  "Perhaps you don't want to %1.",
    "Do you want to be able to %1?",
    "If you could %1, would you?"]],
  
  [r'You are (.*)',
  [  "Why do you think I am %1?",
    "Does it please you to think that I'm %1?",
    "Perhaps you would like me to be %1.",
    "Perhaps you're really talking about yourself?"]],
  
  [r'You\'?re (.*)',
  [  "Why do you say I am %1?",
    "Why do you think I am %1?",
    "Are we talking about you, or me?"]],
  
  [r'I don\'?t (.*)',
  [  "Don't you really %1?",
    "Why don't you %1?",
    "Do you want to %1?"]],
  
  [r'I feel (.*)',
  [  "Good, tell me more about these feelings.",
    "Do you often feel %1?",
    "When do you usually feel %1?",
    "When you feel %1, what do you do?"]],
  
  [r'I have (.*)',
  [  "Why do you tell me that you've %1?",
    "Have you really %1?",
    "Now that you have %1, what will you do next?"]],
  
  [r'I would (.*)',
  [  "Could you explain why you would %1?",
    "Why would you %1?",
    "Who else knows that you would %1?"]],
  
  [r'Is there (.*)',
  [  "Do you think there is %1?",
    "It's likely that there is %1.",
    "Would you like there to be %1?"]],
  
  [r'My (.*)',
  [  "I see, your %1.",
    "Why do you say that your %1?",
    "When your %1, how do you feel?"]],
  
  [r'You (.*)',
  [  "We should be discussing you, not me.",
    "Why do you say that about me?",
    "Why do you care whether I %1?"]],
    
  [r'Why (.*)',
  [  "Why don't you tell me the reason why %1?",
    "Why do you think %1?" ]],
    
  [r'I want (.*)',
  [  "What would it mean to you if you got %1?",
    "Why do you want %1?",
    "What would you do if you got %1?",
    "If you got %1, then what would you do?"]],
  
  [r'(.*) mother(.*)',
  [  "Tell me more about your mother.",
    "What was your relationship with your mother like?",
    "How do you feel about your mother?",
    "How does this relate to your feelings today?",
    "Good family relations are important."]],
  
  [r'(.*) father(.*)',
  [  "Tell me more about your father.",
    "How did your father make you feel?",
    "How do you feel about your father?",
    "Does your relationship with your father relate to your feelings today?",
    "Do you have trouble showing affection with your family?"]],

  [r'(.*) child(.*)',
  [  "Did you have close friends as a child?",
    "What is your favorite childhood memory?",
    "Do you remember any dreams or nightmares from childhood?",
    "Did the other children sometimes tease you?",
    "How do you think your childhood experiences relate to your feelings today?"]],
    
  [r'(.*)\?',
  [  "Why do you ask that?",
    "Please consider whether you can answer your own question.",
    "Perhaps the answer lies within yourself?",
    "Why don't you tell me?"]],
  
  [r'quit',
  [  "Thank you for talking with me.",
    "Good-bye.",
    "Thank you, that will be $150.  Have a good day!"]],
  
  [r'(.*)',
  [  "Please tell me more.",
    "Let's change focus a bit... Tell me about your family.",
    "Can you elaborate on that?",
    "Why do you say that %1?",
    "I see.",
    "Very interesting.",
    "%1.",
    "I see.  And what does that tell you?",
    "How does that make you feel?",
    "How do you feel when you say that?"]]
  ]

#----------------------------------------------------------------------
#  command_interface
#----------------------------------------------------------------------
def command_interface():
  print "Therapist\n---------"
  print "Talk to the program by typing in plain English, using normal upper-"
  print 'and lower-case letters and punctuation.  Enter "quit" when done.'
  print '='*72
  print "Hello.  How are you feeling today?"
  s = ""
  therapist = eliza();
  while s != "quit":
    try: s = raw_input(">")
    except EOFError:
      s = "quit"
      print s
    while s[-1] in "!.": s = s[:-1]
    print therapist.respond(s)


if __name__ == "__main__":
  command_interface()
