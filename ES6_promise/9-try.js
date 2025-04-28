/* eslint-disable */

export default function guardrail(mathFunction) {
	const queue = [];
	const msg = "Guardrail was processed";
	try {
		const result = mathFunction(); 
		queue.push(result);           
	  } catch (err) {
		queue.push('Error: '+ err.message.toString());      
	  }
	  
	  queue.push(msg);
	return queue;
}