import gap_text from './res.json';
import { useEffect, useState } from 'react';
import './Card.css';

function Card() {
  
  const [answers, setAnswers] = useState([]);
  const [results, setResults] = useState([]);
  const [finished, setFinished] = useState(false);
  const [solution, setSolution] = useState(<></>);
  const [_gapText, _setGapText] = useState(gap_text);

  useEffect(() => {
    // API-Aufruf
    const response = fetch('http://127.0.0.1:5000/gap_text', {
      method: 'GET',
    }).then((res) => {
      res.json().then((data) => {
        console.log(data);
        _setGapText(data);
        setAnswers(new Array(data.solutions.length));
      })
    });
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
      _results[i] = answers[i] === _gapText.solutions[i];
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
          _gapText.text.split("<--->").map((item, index, array) => {
            if (index < array.length - 1) 
              return (
                <>
                  <p>{item}<u className={results[index] ? 'card-correct' : 'card-incorrect'}>{_gapText.solutions[index]}</u><b>-</b></p>
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
          _gapText.text.split("<--->").map((item, index, array) => {
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
