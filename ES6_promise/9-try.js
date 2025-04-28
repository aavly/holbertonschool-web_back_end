/* eslint-disable */

export default function guardrail(mathFunction) {
	const queue = [];
	const msg = "Guardrail was processed";
	try {
		queue.push(mathFunction);
		queue.push(msg);
	}
	catch(err) {
		queue.push(err);
		queue.push(msg);
	}
	return queue;
}