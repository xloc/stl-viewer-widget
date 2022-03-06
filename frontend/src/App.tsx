import classNames from 'classnames';
import { useState } from 'react';

function App() {
  const [count, setCount] = useState(0);

  return (
    <div className="flex h-screen justify-center items-center">
      <div className='flex flex-col items-center'>
        <h1 className="text-5xl">Hello World!</h1>
        <button
          className='text-3xl text-white bg-blue-500 w-[10rem] p-2 rounded-full mt-2 select-none'
          onClick={() => (setCount(count + 1))}
        >
          {count}
        </button>
      </div>

    </div >
  );
}

export default App;
