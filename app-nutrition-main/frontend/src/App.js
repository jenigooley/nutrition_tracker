import React from 'react';
import logo from './logo.svg';
import './App.css';
import burger from './mensis-burger.jpg'

const App = React.createClass({
  getInitialState(){
    return {
      user: {
        name: '',
        weight: '',
        height: ''
      },
      events: {
        category: '',
        pain: '',
        flow_amount: ''
      },

      food: '',

    foodChoices: Array.from(Array(3)).map(() => {
      return{
        foodName: '',
        calories: '',
      }
    }),

    displayChoices: false,

    nutrition:{
      name: 'name',
      calories: '',
      sugar: '',
      fat: '',
      protein: '',
      fiber: '',
      calcium: ''
     }
   };
  },

  postFood(e){
    e.preventDefault()
    const data ={choice:1, count: 2, food: this.state.food}
    console.log(this.state.food)
    fetch('/food/jeni', {
      method: 'POST',
      body: JSON.stringify(data),
      headers: new Headers({
          'Content-Type': 'application/json'
      })
    }).then(response => {
        return response.json();
    }).then(json => {
      debugger
      this.setState({
        displayChoices: true,
        foodChoices:[json[0], json[1], json[2]].map(option => {
          return{
            foodName: option[0],
            calories: option[1]
          }
        })
        });
    });
  },

  // postEvent(e){
  //   e.preventDefault()
  //   const data ={category: this.state.category,
  //                pain: this.state.pain,
  //                flow_amount: this.state.flow_amount}
  //   console.log(this.state.category)
  //   fetch('/events/jeni', {
  //     method: 'POST',
  //     body: JSON.stringify(data),
  //     headers: new Headers({
  //         'Content-Type': 'application/json'
  //     })
  //   }).then(response => {
  //       return response.json();
  //   })
  // },

  foodChange(e){
    this.setState({
      food: e.target.value
    })
  },

  categoryChange(e){
    this.setState({
      category: e.target.value
    })
  },

  toggleDisplayChoices(){
    const toggle = !this.state.displayChoices
    this.setState({
      displayChoices: toggle
    })
  },

  componentDidMount(){
    fetch('/users/jeni')
    .then(response => {
      return(
      response.json())
    }).then(json => {
      this.setState({user: json})
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

          <FoodInput
            changeCallback={this.foodChange}
            submitCallback={this.postFood}
            food={this.state.food}
            />

          <FoodChoices
            toggleDisplayChoices={this.toggleDisplayChoices}
            displayChoices={this.state.displayChoices}
            options={this.state.foodChoices}
          />

          <Nutrition
            name={this.name}
            calories={this.state.calories}
            sugar={this.state.sugar}
            fat={this.state.fat}
            protein={this.state.protein}
            fiber={this.state.fiber}
            calcium={this.state.calcium}
            />

          <EventsInput
            changeCallback={this.eventChange}
            submitCallback={this.postEvent}
          />

          <Events
            category={this.state.events.category}
            pain={this.state.events.pain}
            flow_amount={this.state.events.flow_amount}
          />
          <img className='burger-image' src={burger}/>
      </div>
    );
  }
})


const UserInfo = (props) => {
  return(
    <div className='user-box'>
      <p>{props.name}</p>
      <p>weight: {props.weight}</p>
      <p>height: {props.height}</p>
    </div>
  )
}

const EventsInput = (props) => {
  return(
    <form onSubmit={props.submitCallback}>
      <select onChange={props.changeCallback}>
        <option value={props.category}>period</option>
        <option value={props.category}>sex</option>
      </select>
      <br/>
      <input  type="range" min="1" max="5" value={props.pain} onChange={props.changeCallback}/>
      <br/>
      <input  type="range" min="1" max="5" value={props.flow_amount} onChange={props.changeCallback}/>
    </form>
  )
}

const Events = (props) => {
  return (
    <div className='event-box'>
      <p>{props.category}</p>
      <p>pain: {props.pain}</p>
      <p>flow: {props.flow_amount}</p>
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

const FoodChoices = React.createClass({
  getInitialState(){
    return{
      foodName: '',
      count: ''
    }
  },

  optionChange(e){
    this.setState({
      foodName:e.target.value
    })
  },

  countChange(e){
    this.setState({
      count:e.target.value
    })
  },

  postChoice(e){
    e.preventDefault()
    const data ={choice:this.state.foodName, count: this.state.count}
    debugger
    fetch('/food/jeni/count', {
      method: 'POST',
      body: JSON.stringify(data),
      headers: new Headers({
          'Content-Type': 'application/json'
      })
    }).then(response => {
      if(!response.ok){
        throw Error(response.statusText);
      }
    }).then(response => {
      this.props.toggleDisplayChoices()
    }).catch(error => {
      console.log(error)
    })
  },

  render(){
    let optionsRender = (
      <div></div>
    );
    if(this.props.displayChoices){
      optionsRender = (
        <form onSubmit={this.postChoice}>
          <input type='text' name='count' placeholder='Serving Amount' onChange={this.countChange}/>
          {this.props.options.map((option, i) => {
            return(
              <FoodChoice
                key={i}
                foodId={i}
                optionChange={this.optionChange}
                foodName={option.foodName}
                calories={option.calories}
              />
            )
          })}
        </form>
      );
    }
    return optionsRender
  }
});

const FoodChoice = (props) => {
  return(
    <div className='food-choice-box'>
      <label>
      <input type='radio' value={props.foodId} onChange={props.optionChange}/>
      <p>{props.foodName}</p>
      <p>{props.calories}</p>
      </label>
    </div>
  )
}

const Nutrition = (props) => {
  return(
    <div className='nutrition-box'>
      <p>name: {props.name}</p>
      <p>calories: {props.calories}</p>
      <p>sugar: {props.name}</p>
      <p>fat: {props.name}</p>
      <p>protein: {props.name}</p>
      <p>fiber: {props.name}</p>
      <p>calcium: {props.name}</p>
    </div>
  )
}



export default App;
