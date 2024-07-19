from menuPackage.MenuInterface import MenuInterface
from menuPackage.MenuOption import ExitMenuOption
from newsPackage.NewsMenuOption import GetNewsMenuOption


if __name__ == "__main__":
    
  from transformers import pipeline

  summarizer = pipeline("summarization")
  article = """
  Biden's bruising day sinks hopes Democrats will move onThe most devastating argument against Joe Biden’s re-election bid may have come not from a politician or a pundit, but from a film star.
But George Clooney, with his stinging New York Times opinion piece, isn’t the only one speaking out. A growing chorus from Democrats is sinking the president’s hopes of steadying his campaign this week - and perhaps ever.
This all comes after it appeared that the president had turned a corner, with the influential Congressional Black Caucus and key liberal members of Congress just voicing their support for him.
But now the ground has shifted once again - and all in the midst of a high-profile Nato summit with US allies here in Washington.
On Wednesday evening, Peter Welch of Vermont became the first Democratic senator to openly call on Mr Biden to withdraw, "for the good of the country", as he wrote in a newspaper op-ed.
The drumbeat of defections makes the stakes for Mr Biden’s press conference at the end of the Nato summit on Thursday afternoon even higher. It will be the biggest unscripted test for him since his botched debate two weeks prior which triggered this crisis.
Mr Biden also has a sit-down interview scheduled with NBC News presenter Lester Holt on Monday. A fumble or misstep in the days ahead could buttress all the most damaging assertions Mr Clooney, a top Democratic fundraiser, makes in his New York Times piece.
The actor writes that the president's decline is not an illusion; it’s real. He points to a Los Angeles fundraiser he threw for the president last month. “The Joe Biden I was with three weeks ago at the fundraiser was not the Joe... of 2010,” he writes. “He wasn’t even the Joe Biden of 2020. He was the same man we all witnessed at the debate.”
The president is not up to the task of beating Donald Trump in November, Clooney continues. He calls the Biden campaign’s claim that he is the choice of Democratic primary voters “disingenuous, at best”. And, perhaps most devastating, he says every prominent Democrat he has spoken with knows all this – whether they’re willing to publicly admit it or not.
“We can put our heads in the sand and pray for a miracle in November", he writes, “or we can speak the truth.”
The Biden campaign is pushing back against the Clooney piece, noting that the president had flown across nine time zones, from the G7 summit in Italy, to attend the star’s fundraiser.
Campaign officials also note that the president has had serious disagreements recently with the star and his wife, human rights lawyer Amal Clooney, about his administration’s Gaza policy. The opinion piece, published three weeks after that Los Angeles fundraiser, could be viewed like a strike timed for maximum effect.
But Clooney isn’t just any movie star. He’s a powerful fundraiser for Democrats and has been for years. Given that California, and the Hollywood industry in particular, is a key part of the party’s money base, Clooney’s comments present a very real threat to Mr Biden.
It also comes on the heels of expressions of dissatisfaction from other big-money Democratic donors, such as Netflix chair Reed Hastings and IAC chair Barry Diller.
The actor is also plugged in to party politics, with close ties to former President Barack Obama. It is difficult to imagine that he would have taken to the pages of the New York Times in such a dramatic way, with a double-barrel blast against the sitting president, without at least some tacit sign-off from prominent Democrats.
Revelling in the Democratic turmoil on Wednesday night, Trump posted to social media about Clooney: "He’s turned on Crooked Joe like the rats they both are."
Increasingly, prominent Democrats are saying things that should give Mr Biden pause. Senator Welch's column in the Washington Post said: "We have asked President Biden to do so much for so many for so long.
"It has required unmatched selflessness and courage. We need him to put us first, as he has done before. I urge him to do it now."
Earlier in the day, hours before the Clooney and Welch opinion pieces published, former Speaker of the House Nancy Pelosi - who still holds considerable influence within the party - stopped notably short of endorsing Mr Biden's bid for re-election.
She said the president’s critics should hold their tongues until after this week’s Nato summit. “Whatever you're thinking,” she said, “you didn't have to put that out on the table until we see how we go this week.”
She added that Mr Biden should make a decision quickly about whether to continue his campaign. When prodded that the president had already clearly said he would stay in the race, she dodged. “I want him to do whatever he decides to do,” Mrs Pelosi said.
And later in the day, Virginia Senator Tim Kaine - Hillary Clinton’s vice-presidential running mate in 2016 - offered similar lines, about how the president “will do the patriotic thing for the country” and “make that decision”.
Congresswoman Pramila Jayapal of Washington, chair of the Congressional Progressive Caucus, put it even more bluntly: “I’m fully behind him as our nominee until he’s not our nominee.”
It’s as if Mr Biden’s tepid supporters simply won’t take “yes, I’m still running” as an answer. Meanwhile, even some of Mr Biden’s staunchest supporters have started to engage in “what if” scenarios. California Governor Gavin Newsom said he still backs the president, and would not run against Vice-President Kamala Harris as the nominee if Mr Biden stepped aside.
Senate Democrats are meeting Biden campaign officials on Thursday to discuss the future of the campaign. And House minority leader Hakeem Jeffries said he would speak to the president directly about Democratic concerns by Friday.
Wheels are turning, but it's unclear whether they are grinding toward a resolution or spinning in place.
If Mr Biden were to bow out, it’s still unclear what happens next. Some have suggested that Ms Harris, as the president’s running mate, is next in line.
The solution, according to Clooney, is for Democrats to regroup and pick a new nominee, although he is vague about how the process could unfold. And his suggestion that, because of the shortened campaign season, whoever the party chooses would be able to avoid opposition research and negative campaigning – either from fellow Democrats or Republicans – seems naive in the extreme.
While the mood in Washington has taken a new turn against the president in the past 24 hours, the mathematics of his situation has not changed.
Mr Biden still controls the lion’s share of national convention delegates who ultimately decide the party’s presidential ticket. And while those delegates aren’t explicitly bound to support him, he could replace any who show insufficient loyalty.
The opinion polls, while indicating he is trailing Trump, have not changed dramatically since his ill-fated debate. And few show any of the most obvious alternatives to him – the vice-president and prominent Democratic governors – doing substantially better.
Even Mr Biden’s critics, with their appeals to his patriotism, sense of duty and concern for American democracy given the potential for a second Trump presidency, implicitly acknowledge that the decision ultimately lies with him.
What Wednesday demonstrated, though, is that if he presses ahead, he may never be able to fully put the concerns about his age behind him.
His debate performance may end up being a self-inflicted wound that never heals."""
  summary = summarizer(article, max_length=150, min_length=40, do_sample=False)
  print(summary[0]['summary_text'])



    # menu = MenuInterface("Clipboard Manager", 
    #                      "Select an option: ",
    #                      [GetNewsMenuOption(),
    #                       ExitMenuOption()]
    #                     )
    # menu.UtiliseMenu()