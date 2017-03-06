import React from 'react';
import logo from './logo.svg';
import './App.css';

const App = React.createClass({
  getInitialState(){
    return {
      user: {
        name: '',
        weight: '',
        height: ''
      },
      events: {
        category: 'period',
        pain: 0,
        flow_amount: 0
      },
      food: ''

    }
  },

  postFood(e){
    e.preventDefault()
    const data ={choice:1, count: 2, food: this.state.food}
    fetch('/food/jeni', {
      method: 'POST',
      body: data
    })
  },

  foodChange(e){
    this.setState({
      food: e.target.value
    })
  },

  componentDidMount(){
    fetch('/users/jeni')
    .then(response => {
      response.json().then(json => {
      this.setState({user: json})
      })
    })
    // fetch('/events/jeni?category=period&date=02-20-2017')
    // .then(response => {
    //   response.json().then(json => {
    //   this.setState({events: json})
    //   })
    // })
  },

  render() {
    return (
      <div className='App'>
        <UserInfo
          name={this.state.user.name}
          weight={this.state.user.weight}
        height={this.state.user.height}
        />
        <Events
          category={this.state.events.category}
          pain={this.state.events.pain}
          flow_amount={this.state.events.flow_amount}
        />
        <FoodInput
          changeCallback={this.foodChange}
          submitCallback={this.postFood}
          food={this.state.food}
          />

      </div>
    );
  }
})


const UserInfo = (props) => {
  return(
    <div className='userBox'>
      <p>{props.name}</p>
      <p>weight {props.weight}</p>
      <p>height {props.height}</p>
    </div>
  )
}

const Events = (props) => {
  return (
    <div className='eventBox'>
      <p>{props.category}</p>
      <p>pain {props.pain}</p>
      <p>flow {props.flow_amount}</p>
    </div>
  )
}

const FoodInput = (props) => {
  return(
  <form onSubmit={props.submitCallback}>
  <input type='text' value={props.food} onChange={props.changeCallback}/>
  </form>
 )
}


export default App;
