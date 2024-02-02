import {Controller} from '@hotwired/stimulus';

export default class extends Controller {
  static values = {
    count: { type: Number, default: 0 },
  };

  connect() {
    this.element.innerHTML = 'Click me';
  }

  countValueChanged(value, previousValue) {
    console.log(`${previousValue} changed to ${value}`);
  }

  increment(){
    this.countValue++;
    this.element.innerHTML = `You clicked ${this.countValue} times`;
  }
}