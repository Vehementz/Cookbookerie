import { test, it, expect } from 'vitest'

import { add } from './src/math.js';


it('shold summarize all number values in an array', () => {
    const result = add([1,2,3]); 
    expect(result).toBe(6);
});


