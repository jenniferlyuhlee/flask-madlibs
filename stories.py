"""Madlibs Stories."""


class Story:
    """Madlibs story.

    To  make a story, pass a story_type, list of prompts, and the text
    of the template.

        >>> s = Story("Short", ["noun", "verb"],
        ...     "I love to {verb} a good {noun}.")

    To generate text from a story, pass in a dictionary-like thing
    of {prompt: answer, promp:answer):

        >>> ans = {"verb": "eat", "noun": "mango"}
        >>> s.generate(ans)
        'I love to eat a good mango.'
    """

    def __init__(self, story_type, words, text):
        """Create story with words and template text."""

        self.story_type = story_type
        self.prompts = words
        self.template = text

    def generate(self, answers):
        """Substitute answers into text."""

        text = self.template

        for (key, val) in answers.items():
            text = text.replace("{" + key + "}", val)

        return text


# Here's a story to get you started
story_list = [
    Story(
        'Old Tale',
        ["place", "noun", "verb", "adjective", "plural_noun"],
        """Once upon a time in a long-ago {place}, there lived a
        large {adjective} {noun}. It loved to {verb} {plural_noun}."""
    ),

    Story(
        'Fable',
        ["noun_1", "noun_2", "verb_1", "verb_2"],
        """They say that when {noun_1} and {noun_2} {verb_1}, their luck begins to {verb_2}."""
    ),

    Story(
        'Last Night',
        ["place", "noun", "verb", "adjective"],
        """Last night was {adjective}. We went to {place} and saw a {noun} {verb}."""
    ),

    Story(
        'Simple',
        ["noun", "verb", "adjective"],
        """I am a {adjective} {noun}. I love to {verb}."""
    )
]

#story dictionary
stories = {story.story_type: story for story in story_list}



