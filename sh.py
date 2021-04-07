Дана база данных произведений Шекспира, в которой содержатся следующие таблицы:
character – герои произведений, work – произведения, chapter - главы произведений,
paragraph – параграфы, wordform – слова, встречающиеся в произведениях


1. SELECT plaintext, occurences FROM wordform ORDER BY occurences DEsc lIMIT 10;

2. SELECT plaintext FROM wordform WHERE plaintext ILIKE 'a%';

3. SElECT title FROM work WHERE genretype='p';

4. SELECT AVG(totalparagraphs) FROM work where genretype='t';
        
5. SELECT title FROM work WHERE totalwords > (SELECT AVG(totalwords) FROM work);

6. SELECT c.charname, c.speechcount, w.title FROM character AS c JOIN character_work AS cw ON c.charid = cw.charid JOIN work AS w ON cw.workid = w.workid;  

7. SELECT AVG(c.speechcount) FROM character AS c JOIN character_work AS cw ON c.charid = cw.charid JOIN work AS w ON cw.workid = w.workid WHERE title = 'Romeo and Juliet';

8. SELECT SUM(wordcount) FROM paragraph GROUP BY section;

9. SELECT charname FROM character WHERE speechcount BETWEEN 15 AND 30;

10. SELECT title, year FROM work WHERE year BETWEEN 1601 AND 1700;

11. SELECT longtitle FROM work WHERE longtitle ilike '%the%';

12. SELECT DISTINCT section FROM paragraph;

13. SELECT c.chapterid, c.chapter, c.description, w.title FROM chapter AS c JOIN work as w ON c.workid = w.workid;

14. SELECT p.paragraphnum, c.charname, c.speechcount FROM paragraph AS p JOIN character AS c ON p.charid = c.charid;

15. SELECT p.paragraphnum, w.title, w.year FROM paragraph AS p JOIN work AS w ON p.workid = w.workid;
