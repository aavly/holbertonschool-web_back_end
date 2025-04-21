/* eslint-disable */

const createInt8TypedArray = (length, position, value) => {
	const buffer = new ArrayBuffer(length);
	const view = new Uint8Array(buffer);

	view[position] = value;

	return buffer;
};

export default createInt8TypedArray;