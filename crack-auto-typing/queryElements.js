words = document.querySelectorAll('span.test-word.undefined');
wordsContent = [];
words.forEach(function (value) {
    wordsContent.push(value.textContent)
});

// noinspection JSAnnotator
return wordsContent;
