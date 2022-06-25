import gap_text from './res.json';
import { useEffect, useRef, useState } from 'react';
import './Card.css';

function Card() {
  
  const [answers, setAnswers] = useState([]);
  const [results, setResults] = useState([]);
  const [finished, setFinished] = useState(false);
  const [solution, setSolution] = useState(<></>);

  useEffect(() => {
    // API-Aufruf
    // ...

    setAnswers(new Array(gap_text.solutions.length));
  }, []);

  useEffect(() => {
    getSolution();
  }, [finished]);

  function onInputChange(e, index) {
    const newAnswers = new Array(answers.length);
    
    for (let i = 0; i < answers.length; i++) {
      newAnswers[i] = answers[i];
    }

    newAnswers[index] = e.target.value;

    setAnswers(newAnswers);
  }

  function onSubmit() {
    const _results = new Array(answers.length);
    for (let i = 0; i < answers.length; i++) {
      _results[i] = answers[i] === gap_text.solutions[i];
    }
    console.log(_results);
    setResults(_results);
    setFinished(true);
  }

  function getSolution() {
    if (finished) setSolution(
    <div className='card-solution'>
      <div className='card-text'>
        { 
          gap_text.text.split("<--->").map((item, index, array) => {
            if (index < array.length - 1) 
              return (
                <>
                  <p>{item}<u className={results[index] ? 'card-correct' : 'card-incorrect'}>{gap_text.solutions[index]}</u><b>-</b></p>
                </>
              )
            else return (
              <>
                <p>{item}</p>
              </>
            )
          })
        }
      </div>
        <button onClick={(e) => {
          window.location.reload(false);
        }}>Next</button>
      </div>
    );
    else setSolution(<></>);
  }

  return (
    <div className="card">
      <div className='card-text'>
        { 
          gap_text.text.split("<--->").map((item, index, array) => {
            if (index < array.length - 1) 
              return (
                <>
                  <p>{item}</p>
                  <input key={item + index} type="text" onChange={ (e) => { onInputChange(e, index); }} className='userInput' />
                </>
              )
            else return (
              <>
                <p>{item}</p>
              </>
            )
          })
        }
      </div>
      <button type="button" onClick={onSubmit}> Submit </button>
      {solution}
    </div>
  );
}

export default Card;
